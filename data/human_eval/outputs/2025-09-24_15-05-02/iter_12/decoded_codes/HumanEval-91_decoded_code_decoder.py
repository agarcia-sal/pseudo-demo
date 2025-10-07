import re

def is_bored(input_string: str) -> int:
    sentences = re.split(r'[.?!]\s*', input_string)
    count_boredoms = 0
    for sentence in sentences:
        if sentence.startswith('I '):
            count_boredoms += 1
    return count_boredoms