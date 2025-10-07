import re

def is_bored(S) -> int:
    sentences = re.split(r'[.?!]\s*', S)
    count = sum(1 for sentence in sentences if sentence.startswith('I '))
    return count