import re
from typing import List

def is_bored(str_input: str) -> int:
    fragments: List[str] = re.split(r'[.?!]\s*', str_input)
    count_bored: int = 0
    idx: int = 0
    while idx < len(fragments):
        segment: str = fragments[idx]
        if segment.startswith('I '):
            count_bored += 1
        idx += 1
    return count_bored