from lib.diary_entry_class import DiaryEntry

class Diary:
    def __init__(self):
        self.all_entries = []

    def add(self, entry):
        self.all_entries.append(entry)

    def all(self):
        return self.all_entries

    def count_words(self):
        word_count = 0
        for entry in self.all():
            word_count += entry.count_words()
        return word_count
        

    def reading_time(self, wpm):
        return round(self.count_words() / wpm)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        max_length = wpm * minutes
        sort_key = lambda entry: entry.count_words()
        entries_by_length_descending = sorted(self.all(), key=sort_key , reverse=True)
        for entry in entries_by_length_descending:
            if not entry.count_words() > max_length:
                return entry


        
