from dataclasses import dataclass

@dataclass
class DiaryEntry():
    title: str
    contents: str

    def format(self):
        return f"{self.title}: {self.contents}"
