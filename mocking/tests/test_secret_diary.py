from unittest.mock import Mock
from lib.secret_diary import SecretDiary

"""
When initialising with a diary
Secret diary is set to locked
"""
def test_init_sets_diary_as_locked():
    fake_diary = Mock()
    secret_diary = SecretDiary(fake_diary)
    assert secret_diary._is_locked == True

"""
Calling read() for a locked diary
Raises the error "Go away!"
"""
def test_read_raises_error_for_locked_diary():
    fake_diary = Mock()
    secret_diary = SecretDiary(fake_diary)
    assert secret_diary.read() == "Go away!"  

"""
after calling unlock()
read() returns the contents of a diary
"""
def test_unlock_and_read():
    fake_diary = Mock()
    fake_diary.read.return_value = "some contents"
    secret_diary = SecretDiary(fake_diary)
    secret_diary.unlock()
    assert secret_diary.read() == "some contents"

"""
after locking and unloacked diary
read() returns "Go away!" 
"""
def test_lock_diary():
    fake_diary = Mock()
    fake_diary.read.return_value = "some contents"
    secret_diary = SecretDiary(fake_diary)
    secret_diary.unlock()
    secret_diary.lock()
    assert secret_diary.read() == "Go away!"
