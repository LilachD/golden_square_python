import pytest
from lib.class_grammar_stats import *

# CHECK
# returns: true if the text begins with a capital letter 
# and ends with a sentence-ending punctuation mark, false otherwise

# return error message for non-string or empty string.
def test_check_returns_error_message_for_non_or_empty_string():
    grammar_stats = GrammarStats()
    with pytest.raises(Exception) as e:
        grammar_stats.check(5)
    assert str(e.value) == 'Can\'t read that. Please enter a non-empty string.'
    with pytest.raises(Exception) as e:
        grammar_stats.check('')
    assert str(e.value) == 'Can\'t read that. Please enter a non-empty string.'

# return True for grammatically correct string i.e starts with Capital, ends with suitable punctuation
def test_check_returns_true_for_correct_grammar():
    grammar_stats = GrammarStats()
    assert grammar_stats.check('Hello!') == True
    assert grammar_stats.check('What are you up to today?') == True

# return False for all other non-empty strings
def test_check_returns_false_for_incorrect_grammar():
    grammar_stats = GrammarStats()
    assert grammar_stats.check('sup?') == False
    assert grammar_stats.check('Hello there,') == False


# PERCENTAGE_GOOD
# returns int: the percentage of texts checked so far that passed the check
# defined in the `check` method. The number 55 represents 55%.

# returns error message if no checks have been made so far
def test_percentage_good_reurns_error_if_none_checked():
    grammar_stats = GrammarStats()
    with pytest.raises(Exception) as e:
        grammar_stats.percentage_good()
    assert str(e.value) == 'No text has been checked so far'

def test_percentage_good_returns_persentage_as_int_of_correct_texts():
    grammar_stats = GrammarStats()
    grammar_stats.check('Hello!')
    grammar_stats.check('What are you up to today?')
    grammar_stats.check('sup?')
    assert grammar_stats.percentage_good() == 67
