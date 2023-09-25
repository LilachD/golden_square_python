import re

class PhoneNumberExtractor():
    def __init__(self, diary):
        self._entries = diary._all_entries

    def extract(self):
        all_numbers = set()
        for entry in self._entries:
            all_numbers.update(re.findall(r"\b0[0-9]{10}\b", entry.contents))
        if all_numbers == set():
            return "No phone numbers found"
        return all_numbers
            
