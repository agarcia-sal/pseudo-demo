import re
from typing import List


def is_bored(input_string: str) -> int:
    sentence_collection: List[str] = re.split(r'[.?!]\s*', input_string)
    accumulator: int = 0
    for index in range(len(sentence_collection)):
        if sentence_collection[index].startswith('I '):
            accumulator += 1
    return accumulator