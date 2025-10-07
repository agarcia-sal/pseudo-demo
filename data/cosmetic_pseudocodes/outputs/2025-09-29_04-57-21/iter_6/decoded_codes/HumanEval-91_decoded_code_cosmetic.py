import re
from typing import List


def is_bored(input_string: str) -> int:
    sentences_array: List[str] = re.split(r'[.?!]\s*', input_string)
    tally: int = 0
    for each_phrase in sentences_array:
        if each_phrase.startswith('I '):
            tally += 1
    return tally