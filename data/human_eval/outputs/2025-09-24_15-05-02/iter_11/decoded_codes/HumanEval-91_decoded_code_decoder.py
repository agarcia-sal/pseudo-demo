import re

def is_bored(string_S):
    sentences = re.split(r'[.?!]\s*', string_S)
    boredom_count = 0
    for sentence in sentences:
        if sentence.startswith('I '):
            boredom_count += 1
    return boredom_count