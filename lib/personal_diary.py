
def make_snippet(string):
    words = string.split(" ")
    if len(words) > 5:
        return " ".join(words[slice(5)]) + "..."
    return string

def count_words(string):
    if not len(string):
        return 0
    return len(string.split(" "))