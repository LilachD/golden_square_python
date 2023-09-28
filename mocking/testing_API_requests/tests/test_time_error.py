import time
from unittest.mock import Mock
from lib.time_error import TimeError

def test_time_error_returns_difference_between_times():
    requester_mock = Mock()
    timer_mock = Mock()

    requester_mock.get.return_value.json.return_value = {
        "dst_until":"2023-10-29T01:00:00+00:00",
        "raw_offset":0,
        "timezone":"Europe/London",
        "unixtime":1695735736,
        "utc_datetime":"2023-09-26T13:42:16.472448+00:00",
        "utc_offset":"+01:00",
        "week_number":39
        }
    
    timer_mock.time.return_value = 1695735736.5

    time_error = TimeError(requester_mock, timer_mock)
    assert time_error.error() == -0.5

