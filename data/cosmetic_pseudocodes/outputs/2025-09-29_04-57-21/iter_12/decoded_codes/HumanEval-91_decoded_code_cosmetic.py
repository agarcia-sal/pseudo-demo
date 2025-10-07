import re
from typing import List


def is_bored(input_string: str) -> int:
    parts: List[str] = re.split(r'[.?!]\s*', input_string)
    tally: int = 0
    index: int = 0
    while index < len(parts):
        segment = parts[index]
        if segment.startswith('I '):
            tally += 1
        index += 1
    return tally