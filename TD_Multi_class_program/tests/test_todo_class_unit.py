from lib.todo_class import *

def test_init_a_task_as_incomplete():
    my_task = Todo('hang up washing')
    assert my_task.complete == False

def test_mark_complete_sets_complete_to_True():
    my_task = Todo('pack for trip')
    my_task.mark_complete()
    assert my_task.complete == True

