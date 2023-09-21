import pytest
from lib.class_design_exercise import *


# show_list method returns a list of all tasks added
def test_add_task_and_show_list():
    to_do_list = TODO_List()
    to_do_list.add_task('Water the plants')
    to_do_list.add_task('Go for a run')
    assert to_do_list.show_list() == ['Water the plants', 'Go for a run']

# show_list method returns a list without any completed items
def test_mark_complete_removes_tasks_from_list():
    to_do_list = TODO_List()
    to_do_list.add_task('Water the plants')
    to_do_list.add_task('Go for a run')
    to_do_list.mark_complete('Water the plants')
    assert to_do_list.show_list() == ['Go for a run']

# mark_complete returns 'task not in list' for input that doesn't exist in list
def test_mark_complete_returns_error_for_wrong_input():
    to_do_list = TODO_List()
    to_do_list.add_task('Water the plants')
    with pytest.raises(Exception) as e:
        to_do_list.mark_complete('Wash hair')
    assert str(e.value) == 'Task not in list'

# mark_complete returns confirmation for completed tasks
def test_mark_complete_returns_confirmation_message():
    to_do_list = TODO_List()
    to_do_list.add_task('Water the plants')
    to_do_list.add_task('Go for a run')
    assert to_do_list.mark_complete('Water the plants') == 'Task marked as complete'