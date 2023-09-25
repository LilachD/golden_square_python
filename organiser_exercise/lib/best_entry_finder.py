
class BestEntryFinder():
    def __init__(self, diary):
        self._diary = diary

    def find(self, wpm, minutes):
        max_length = wpm * minutes
        readable_entries = [
            entry for entry in self._diary._all_entries 
            if self.word_count(entry) <= max_length
        ]
        sort_key = lambda entry: self.word_count(entry)
        if readable_entries == []:
            return None
        return max(readable_entries, key=sort_key).format()
            
    def word_count(self, entry):
        return len(entry.contents.split())
        