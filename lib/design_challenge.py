def contains_task(text):
    if not isinstance(text, str) or not len(text):
        raise Exception('Please insert non-empty string')
    return '#TODO' in text