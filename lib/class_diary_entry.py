class DiaryEntry:
    def __init__(self, title, contents):
        if not isinstance(title, str) or not isinstance(contents, str) or not len(title) or not len(contents):
            raise Exception('Error. Please enter some text in quotes.')
        self.title = title
        self.contents = contents
        self.first_word_index = 0

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        return len(self.format().split())

    def reading_time(self, wpm):
        if not isinstance(wpm, int) or wpm < 1:
            raise Exception('Error. Please enter a whole number no smaller than 1.')
        return round(self.count_words() / wpm)

    def reading_chunk(self, wpm, minutes):
        if not isinstance(wpm, int) or not isinstance(minutes, int) or wpm < 1 or minutes < 1:
            raise Exception('Error. Please enter two whole numbers no smaller than 1.')
        if self.first_word_index >= self.count_words():
            self.first_word_index = 0
        last_word_index = self.first_word_index + (wpm * minutes)
        words_in_chunk = self.format().split()[self.first_word_index:last_word_index]
        self.first_word_index = last_word_index
        return ' '.join(words_in_chunk)

