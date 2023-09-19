import pytest
from lib.design_challenge import *

# returns error message for empty string 
def test_contains_task_returns_error_for_empty_string():
    with pytest.raises(Exception) as e:
        contains_task('')
    assert str(e.value) == 'Please insert non-empty string'

# returns error message for non-string argument
def test_contains_task_returns_error_for_non_string():
    with pytest.raises(Exception) as e:
        contains_task(4)
    assert str(e.value) == 'Please insert non-empty string'

# returns True if string contains '#TODO'
def test_contains_task_returns_true_for_todo_string():
    assert contains_task('This is my #TODO list') == True

# returns False is string doesn't contain #TODO
def test_contains_task_returns_false_for_non_todo_string():
    assert contains_task('not a task') == False