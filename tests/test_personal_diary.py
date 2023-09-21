from lib.personal_diary import *

# The make_snippet function takes a string as an argument
# if longer than 5 words, it returns the first 5 words followed by ...
# or the whole string otherwise

# given a string shorter than 6 words it reyurns the string as is
def test_returns_whole_string_if_shorter_than_six_words():
    result0 = make_snippet('')
    result3 = make_snippet('Another day done.')
    result5 = make_snippet('Nothing to write today.')
    assert result0 == ''
    assert result3 == 'Another day done.'
    assert result5 == 'Nothing to write today.'
    

# given a string longer than 5 words, it returns the first 5 followed by "..."
def test_returns_five_word_snippet_for_longer_string():
    result = make_snippet('Last night I went out for dinner with Pinzo.')
    assert result == 'Last night I went out...'


# the count_words function takes a string as an argument 
# returns the number of words in that string

# returns 0 if string is empty
def test_returns_zero_for_empty_string():
    assert count_words('') == 0

# returns number of words if not empty
def test_returns_number_of_words_in_string():
    result1 = count_words('Hi!')
    result5 = count_words('How are you today hun?')
    result13 = count_words('Don\'t worry about a thing, cause every little thing is gonna be alright!')
    assert result1 == 1
    assert result5 == 5
    assert result13 == 13

