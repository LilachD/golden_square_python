class TracksTracker():
    def __init__(self):
        self.track_list = []

    def add_track(self, track):
        if not isinstance(track, str):
            raise Exception("That's not a music track!")
        self.track_list.append(track)

    def show_track_list(self):
        return self.track_list