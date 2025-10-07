import re

def is_bored(S: str) -> int:
    sentences = re.split(r'[.?!]\s*', S)
    count = 0
    for i in range(len(sentences) - 1):
        sentence = sentences[i]
        if len(sentence) >= 2 and sentence[:2] == 'I ':
            count += 1
    return count