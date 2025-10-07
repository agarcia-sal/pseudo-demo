import re
from typing import List


def is_bored(input_string: str) -> int:
    sentences_array: List[str] = re.split(r'[.?!]\s*', input_string)
    accumulator: int = 0
    for sentence in sentences_array:
        if sentence.startswith('I '):
            accumulator += 1
    return accumulator