from lib.diary import Diary

"""
When initialising a diary with contents
diary.read returns the contents
"""
def test_diary_read_returns_contents():
    diary = Diary('some contents')
    assert diary.read() == 'some contents'
