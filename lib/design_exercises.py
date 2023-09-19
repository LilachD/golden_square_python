def estimate_reading_time(text):
    if not isinstance(text, str):
        raise Exception('Can\'t read this! Please insert a string.')
    elif not len(text):
        raise Exception('There is nothing to read!')
    else:
        text_length = len(text.split())
        if text_length % 200:
            return f"Estimated reading time: less than {(text_length // 200) + 1} minutes"
        return f"Estimated reading time: {text_length // 200} minutes"


def grammar_checker(text):
    if not isinstance(text, str) or not len(text):
        raise Exception('Can\'t read that. Please enter a non-empty string.')
    return text[0].isupper() and text[-1] in '!?.'
        
