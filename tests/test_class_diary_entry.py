import pytest
from lib.class_diary_entry import DiaryEntry


# __INIT__
# takes two strings as arguments, title and contents
def test_returns_error_for_unsuitable_input():
    with pytest.raises(Exception) as e:
        diaryEntry = DiaryEntry(5, '')
    assert str(e.value) == 'Error. Please enter some text in quotes.'



# FORMAT
#  returns: A formatted diary entry, for example: "My Title: These are the contents"
def test_format_method_returns_formatted_text():
    diaryEntry = DiaryEntry('Makers Day 3', 'Today we\'re learning about testing classes and debugging')
    assert diaryEntry.format() == 'Makers Day 3: Today we\'re learning about testing classes and debugging'



# COUNT_WORDS 
# returns int: the number of words in the diary entry
def test_count_words_returns_word_count_as_int():
    diaryEntry = DiaryEntry('Makers Day 3', 'Today we\'re learning about testing classes and debugging')
    assert diaryEntry.count_words() == 11



#   READING_TIME
#  returns int: an estimate of the reading time in minutes for the contents at the given wpm.
def test_returns_int_measure_of_time_needed():
    diaryEntry = DiaryEntry('Makers Day 3', 'Today we\'re learning about testing classes and debugging')
    assert diaryEntry.reading_time(8) == 1
    assert diaryEntry.reading_time(5) == 2

# returns error message for floats, 0 and negative numbers
def test_reading_time_returns_error_for_zero_and_under_and_floats():
    diaryEntry = DiaryEntry('Makers Day 3', 'Today we\'re learning about testing classes and debugging')
    with pytest.raises(Exception) as e:
        diaryEntry.reading_time(0)
    assert str(e.value) == 'Error. Please enter a whole number no smaller than 1.'
    with pytest.raises(Exception) as e:
        diaryEntry.reading_time(-2)
    assert str(e.value) == 'Error. Please enter a whole number no smaller than 1.'
    with pytest.raises(Exception) as e:
        diaryEntry.reading_time(1.5)
    assert str(e.value) == 'Error. Please enter a whole number no smaller than 1.'



# READING_CHUNK 
# returns string: a chunk of the contents that the user could read in the given number of minutes.
# If called again, `reading_chunk` should return the next chunk,
# skipping what has already been read, until the contents is fully read.
# The next call after that should restart from the beginning.

# returns an error message if wpm or minutes are not a positive integer 
def test_reading_chunk_returns_error_for_under_one_and_floats():
    diaryEntry = DiaryEntry('Makers Day 3', 'Today we\'re learning about testing classes and debugging')
    with pytest.raises(Exception) as e:
        diaryEntry.reading_chunk(1, 0)
    assert str(e.value) == 'Error. Please enter two whole numbers no smaller than 1.'
    with pytest.raises(Exception) as e:
        diaryEntry.reading_chunk(5, -2)
    assert str(e.value) == 'Error. Please enter two whole numbers no smaller than 1.'
    with pytest.raises(Exception) as e:
        diaryEntry.reading_chunk(2, 1.5)
    assert str(e.value) == 'Error. Please enter two whole numbers no smaller than 1.'

# returns a suitable chunck of text for the time given:
def test_returns_chunk_suitable_for_time_requirement():
    diaryEntry = DiaryEntry('Makers Day 3', 'Today we\'re learning about testing classes and debugging')
    assert diaryEntry.reading_chunk(2, 3) == 'Makers Day 3: Today we\'re learning'

# returns the next chunk:
def test_reading_chunk_returns_next_chunk_of_text():
    diaryEntry = DiaryEntry('Makers Day 3', 'Today we\'re learning about testing classes and debugging')
    diaryEntry.reading_chunk(2, 3)
    assert diaryEntry.reading_chunk(2, 2) == 'about testing classes and'
    assert diaryEntry.reading_chunk(2, 4) == 'debugging'

# goes back to the start once finished
def test_reading_chunk_start_back_from_beginning_once_done():
    diaryEntry = DiaryEntry('Makers Day 3', 'Today we\'re learning about testing classes and debugging stuff.')
    diaryEntry.reading_chunk(2, 2)
    diaryEntry.reading_chunk(2, 4)
    assert diaryEntry.reading_chunk(2, 3) == 'Makers Day 3: Today we\'re learning'

