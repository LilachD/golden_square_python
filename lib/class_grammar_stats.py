class GrammarStats:
    def __init__(self):
        self.checked = 0
        self.passed = 0

    def check(self, text):
        if not isinstance(text, str) or not len(text):
            raise Exception('Can\'t read that. Please enter a non-empty string.')
        self.checked += 1
        if text[0].isupper() and text[-1] in '!?.':
            self.passed += 1
            return True
        return False

    def percentage_good(self):
        if not self.passed:
            raise Exception('No text has been checked so far')
        return round(self.passed / self.checked * 100)