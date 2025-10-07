import re
from typing import List


def is_bored(input_string: str) -> int:
    fragments: List[str] = re.split(r'[?!.]\s*', input_string)
    tally: int = 0
    iterator: int = 0
    while iterator < len(fragments):
        if fragments[iterator].startswith('I '):
            tally += 1
        iterator += 1
    return tally