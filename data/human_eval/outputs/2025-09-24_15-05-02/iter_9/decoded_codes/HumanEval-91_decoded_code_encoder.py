import re

def is_bored(S):
    sentences = re.split(r'[.?!]\s*', S)
    boredom_count = sum(sentence.startswith("I ") for sentence in sentences)
    return boredom_count