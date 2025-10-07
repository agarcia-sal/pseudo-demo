import re
from typing import List


def is_bored(text_input: str) -> int:
    sentence_collection: List[str] = re.split(r'[.?!]\s*', text_input)
    counter: int = 0
    idx: int = 0

    while idx < len(sentence_collection):
        sentence = sentence_collection[idx]
        if sentence[:2] == 'I ':
            counter += 1
        idx += 1

    return counter