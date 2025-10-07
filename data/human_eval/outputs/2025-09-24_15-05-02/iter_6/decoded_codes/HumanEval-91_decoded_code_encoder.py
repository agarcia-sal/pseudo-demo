import re

def is_bored(text_string):
    sentences = re.split(r'[.?!]\s*', text_string)
    boredom_count = 0
    for sentence in sentences:
        if sentence.startswith("I "):
            boredom_count += 1
    return boredom_count