import re
from typing import List


def is_bored(test_text: str) -> int:
    segments: List[str] = re.split(r'[.?!][ \t]*', test_text)
    tally: int = 0
    index: int = 0
    while index < len(segments):
        if segments[index].startswith('I '):
            tally += 1
        index += 1
    return tally