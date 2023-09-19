import pytest
from lib.design_exercises import *

# EXERCISE ONE:

# User Story:
# As a user
# So that I can manage my time
# I want to see an estimate of reading time for a text, 
# assuming that I can read 200 words a minute.

# for testing purposes, a function to generate text of a certain length:
def text_generator(word_count):
    text = []
    for w in range(word_count):
        text.append('word')
    return " ".join(text)

# Function signature:
    # function name: estimate_reading_time

    # Takes arguemnts: a string of text

    # Returns: The estimated reading time rounded up to the nearest ceiling

    # Side effects: If the text is empty, needs to return 0

# Examples:

# Given an empty text, returns 'nothing to read'
def test_returns_error_message_for_empty_string():
    with pytest.raises(Exception) as e:
        estimate_reading_time('')
    assert str(e.value) == 'There is nothing to read!'

# Given a text not divisible by 200, returns an estimate of 'less than' the nearest ceiling
def test_returns_less_than_two_for_300__word_text():
    assert estimate_reading_time(text_generator(300)) == 'Estimated reading time: less than 2 minutes'
    assert estimate_reading_time(text_generator(725)) == 'Estimated reading time: less than 4 minutes'

# Given a text divisible by 200, returns the complementry divisor
def test_returns_two_for_400_word_text():
    assert estimate_reading_time(text_generator(400)) == "Estimated reading time: 2 minutes"
    assert estimate_reading_time(text_generator(2000)) == "Estimated reading time: 10 minutes"

# Given an input that isn't a tring, returns error message
def test_returns_error_message_for_wrong_data_type():
    with pytest.raises(Exception) as e:
        estimate_reading_time(5.6)
    assert str(e.value) == 'Can\'t read this! Please insert a string.'
    with pytest.raises(Exception) as e:
        estimate_reading_time(True)
    assert str(e.value) == 'Can\'t read this! Please insert a string.'


# EXERCISE TWO:

# User Story:
# As a user
# So that I can improve my grammar
# I want to verify that a text starts with a capital letter 
# and ends with a suitable sentence-ending punctuation mark.

# Function signature:
    # function name: grammar_checker

    # Takes arguemnts: a string of text

    # Returns: True for sentences beginning with a capital letter
    #          and ending in ! ? or . 
    #          otherwise returns False

    # Side effects: Error messages for empty strings and non-string input

# Examples:

# return error message for non-string or empty string.
def test_returns_error_message_for_non_or_empty_string():
    with pytest.raises(Exception) as e:
        grammar_checker(5)
    assert str(e.value) == 'Can\'t read that. Please enter a non-empty string.'
    with pytest.raises(Exception) as e:
        grammar_checker('')
    assert str(e.value) == 'Can\'t read that. Please enter a non-empty string.'

# return True for grammatically correct string i.e starts with Capital, ends with suitable punctuation
def test_returns_true_for_correct_grammar():
    assert grammar_checker('Hello!') == True
    assert grammar_checker('What are you up to today?') == True

# return False for all other non-empty strings
def test_returns_false_for_incorrect_grammar():
    assert grammar_checker('sup?') == False
    assert grammar_checker('Hello there,') == False