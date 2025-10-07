import re

def count_sentences_starting_with_I(S):
    sentences = re.split(r'[.?!]', S)
    return sum(1 for sentence in sentences if sentence.strip().startswith('I '))