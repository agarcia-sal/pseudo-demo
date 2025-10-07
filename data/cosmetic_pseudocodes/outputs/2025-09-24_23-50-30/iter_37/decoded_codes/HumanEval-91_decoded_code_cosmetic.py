import re
from typing import List


def is_bored(input_string: str) -> int:
    segments: List[str] = re.split(r'[.?!]\s*', input_string)
    tally: int = 0
    for fragment in segments:
        if fragment.startswith('I '):
            tally += 1
    return tally