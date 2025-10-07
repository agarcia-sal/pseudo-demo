import re
from typing import List


def is_bored(corpus: str) -> int:
    fragments: List[str] = re.split(r'[.?!]\s*', corpus)
    accumulator: int = 0
    index: int = 0
    while index < len(fragments):
        if fragments[index].startswith('I '):
            accumulator += 1
        index += 1
    return accumulator