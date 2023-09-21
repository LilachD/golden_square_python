import pytest
from lib.class_design_challenge import *

def test_add_track_adds_tracks_to_a_list():
    music_tracker = TracksTracker()
    music_tracker.add_track('Britney Spears - Hit Me Baby One More Time')
    music_tracker.add_track('Bill Withers - Lovely Day')
    assert music_tracker.show_track_list() == ['Britney Spears - Hit Me Baby One More Time', 'Bill Withers - Lovely Day']

def test_add_track_returns_error_for_bad_input():
    music_tracker = TracksTracker()
    with pytest.raises(Exception) as e:
        music_tracker.add_track(45)
    assert str(e.value) == "That's not a music track!"

# Other design options:
# init with dictionary storing artist: [tracks]
# show track list could return a formatted list

