import re

def is_bored(S):
    sentences = re.split(r'[.?!]\s*', S)
    return sum(1 for sentence in sentences if sentence.startswith("I "))