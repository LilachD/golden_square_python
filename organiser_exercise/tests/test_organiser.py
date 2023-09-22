from lib.diary_class import *
from lib.diary_entry_class import *
from lib.todo_class import *
from lib.todo_list import *
from lib.organiser import *

"""
organiser.add_diary stores a Diary object inside an instance of Organiser
"""
def test_add_diary_adds_diary():
    organiser = Organiser()
    diary = Diary()
    diary_entry_1 = DiaryEntry('Title 1', 'Contents 1')
    diary.add(diary_entry_1)
    organiser.add_diary(diary)
    assert organiser._diary == diary

"""
organiser.add_todo_list stores a TodoList object inside an instance of Organiser
"""
def test_add_todo_list_adds_todo_list_attribute():
    organiser = Organiser()
    todo_list = TodoList()
    todo_1 = Todo('Task 1')
    todo_list.add(todo_1)
    organiser.add_todo_list(todo_list)
    assert organiser._todo_list == todo_list
