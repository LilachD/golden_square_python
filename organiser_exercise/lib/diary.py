

class Diary:
    def __init__(self):
        self._all_entries = []

    def add(self, entry):
        self._all_entries.append(entry)

    def all(self):
        return [entry.format() for entry in self._all_entries]

