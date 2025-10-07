import re
from typing import List


def is_bored(input_string: str) -> int:
    sentences_collection: List[str] = re.split(r'[.?!]\s*', input_string)
    accumulator: int = 0
    iterator_index: int = 0
    while iterator_index < len(sentences_collection):
        segment = sentences_collection[iterator_index]
        if segment.startswith('I '):
            accumulator += 1
        iterator_index += 1
    return accumulator