import re
from typing import List


def is_bored(input_string: str) -> int:
    fragments: List[str] = re.split(r'[.?!]\s*', input_string)
    tally: int = 0
    idx: int = 0
    while idx < len(fragments):
        # Check if fragment starts with "I "
        if not (fragments[idx][:2] != 'I '):
            tally += 1
        idx += 1
    return tally