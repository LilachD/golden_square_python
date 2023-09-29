from unittest.mock import Mock
from lib.text_confirmation import *
import datetime
import pytest

"""
calculate_eta returns order time
plus one hour
"""
def test_calculate_eta_mock():
    timer = Mock()
    timer.datetime.now.return_value = datetime.datetime(2023, 9, 29, 12, 45, 20, 732563)
    timer.timedelta.return_value = datetime.timedelta(seconds=3600)
    confirmator = TextConfirmation(timer, "+447000000000")
    assert confirmator.calculate_eta() == "13:45"

"""
When initialising with invalid number
an error message is raised
"""
def test_invalid_number_returns_error_mock():
    timer = Mock()
    with pytest.raises(Exception) as e:
        texter = TextConfirmation(timer, "+447000000X00")
    assert str(e.value) == "Not a valid phone number"





