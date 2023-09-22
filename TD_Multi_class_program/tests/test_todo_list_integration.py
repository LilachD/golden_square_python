from lib.todo_class import *
from lib.todo_list import *


def test_incomplete_returns_list_of_incomplete_tasks():
    todo_list = TodoList()
    todo1 = Todo('water the dog')
    todo2 = Todo('take the cat for a walk')
    todo_list.add(todo1)
    todo_list.add(todo2)
    assert todo_list.incomplete() == [todo1, todo2]

def test_give_up_completes_all_tasks():
    todo_list = TodoList()
    todo1 = Todo('water the dog')
    todo2 = Todo('take the cat for a walk')
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.give_up()
    assert todo_list.complete() == [todo1, todo2]
    