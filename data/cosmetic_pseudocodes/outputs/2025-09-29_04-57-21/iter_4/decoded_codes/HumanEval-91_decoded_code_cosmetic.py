import re
from typing import List


def is_bored(input_string: str) -> int:
    fragments: List[str] = re.split(r'[.?!]\s*', input_string)
    tally: int = 0
    iter: int = 0
    while iter < len(fragments):
        segment: str = fragments[iter]
        if segment.startswith('I '):
            tally += 1
        iter += 1
    return tally