import re

def count_sentences_starting_with_I(S):
    Ss = re.split(r'[.?!]\s*', S)
    return sum(1 for s in Ss if s.startswith("I "))