from lib.diary_class import *
from lib.diary_entry_class import *

# When adding 2 entries to a diary
# Diary.all returns a list of diary objects
def test_diary_all_returns_list_of_entry_objects():
    diary = Diary()
    entry1 = DiaryEntry('entry1', 'this is my first entry')
    entry2 = DiaryEntry('entry2', 'this is my second entry')
    diary.add(entry1)
    diary.add(entry2)
    assert diary.all() == [entry1, entry2]


# When adding 2 entries to a diary
# Diary.count_words return the overall number of words in both diary entries 
# (not including titles)
def test_diary_count_words_returns_total_word_count():
    diary = Diary()
    entry1 = DiaryEntry('entry1', 'this is my first entry')
    entry2 = DiaryEntry('entry2', 'this is my second entry')
    diary.add(entry1)
    diary.add(entry2)
    assert diary.count_words() == 10


# When adding 2 entries to a diary 
# and specifing a reading speed (words per minute)
# Diary.reading_time returns an estimate of the number of minutes 
# it would take the user to read all entries in the diary.
def test_diary_reading_time_returns_estimate_for_total():
    diary = Diary()
    entry1 = DiaryEntry('entry1', 'this is my first entry')
    entry2 = DiaryEntry('entry2', 'this is my second entry')
    diary.add(entry1)
    diary.add(entry2)
    assert diary.reading_time(3) == 3


# When specifing wpm and available time in minutes,
# we recieve the longest diary entry that can be read in its entirety
# in the time specified.
def test_diary_best_entry_returns_correct_entry():
    diary = Diary()
    entry1 = DiaryEntry('entry1', 'this is my very first entry')
    entry2 = DiaryEntry('entry2', 'this is my second entry of the day. this is going well so far!')
    entry3 = DiaryEntry('entry3', 'this is another entry, a longer one this time, just to make sure this function really does work as it should')
    diary.add(entry1)
    diary.add(entry2)
    assert diary.find_best_entry_for_reading_time(6, 2) == entry1
    assert diary.find_best_entry_for_reading_time(6, 3) == entry2




