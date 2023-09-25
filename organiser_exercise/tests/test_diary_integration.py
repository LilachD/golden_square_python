from lib.todo import *
from lib.todo_list import *
from lib.best_entry_finder import *
from lib.diary import *
from lib.diary_entry import *
from lib.phone_number_extractor import *

"""
phone number extractor returns a list 
of phone numbers found in 2 diary entries
"""
def test_phone_number_extractor_returns_found_numbers():
    entry1 = DiaryEntry("title1", "Jonathan's new number is 07123456789")
    entry2 = DiaryEntry("title2", "call 07987654321")
    diary = Diary()
    diary.add(entry1)
    diary.add(entry2)
    extractor = PhoneNumberExtractor(diary)
    assert extractor.extract() == {"07987654321", "07123456789"}

"""
phone number extractor returns error message
for diary with no entries
"""
def test_phone_extractor_returns_message_for_empty_diary():
    diary = Diary()
    extractor = PhoneNumberExtractor(diary)
    assert extractor.extract() == "No phone numbers found"

"""
phone number extractor removes duplicate numbers
and disregards invalid numbers
"""
def test_phone_extractor_returns_no_duplicates_or_invalid_numbers():
    entry1 = DiaryEntry("title1", "Jonathan's new number is 07123456789")
    entry2 = DiaryEntry("title2", "call 0798765-000")
    entry3 = DiaryEntry("title3", "07123456789 and 02083334433")
    diary = Diary()
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    extractor = PhoneNumberExtractor(diary)
    assert extractor.extract() == {"07123456789", "02083334433"}

"""
best entry finder returns none if no suitable entries exist
"""
def test_best_entry_finder_returns_none():
    entry1 = DiaryEntry("title1", "1 2 3 4 5 6")
    entry2 = DiaryEntry("title2", "1 2 3 4 5")
    entry3 = DiaryEntry("title3", "1 2 3 4 5 6 7 8 9")
    diary = Diary()
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    entry_finder = BestEntryFinder(diary)
    assert entry_finder.find(2, 2) == None

"""
Best entry finder returns longest readable entry
"""
def test_best_entry_finder_returns_none():
    entry1 = DiaryEntry("title2", "1 2 3 4 5")
    entry2 = DiaryEntry("title3", "1 2 3 4 5 6 7 8 9")
    entry3 = DiaryEntry("title1", "1 2 3 4 5 6")
    diary = Diary()
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    entry_finder = BestEntryFinder(diary)
    assert entry_finder.find(2, 3) == "title1: 1 2 3 4 5 6"