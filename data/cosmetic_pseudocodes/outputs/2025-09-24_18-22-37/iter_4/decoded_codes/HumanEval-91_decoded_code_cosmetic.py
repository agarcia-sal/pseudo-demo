import re
from typing import List

def is_bored(input_text: str) -> int:
    segments: List[str] = re.split(r'[.?!]\s*', input_text)
    total_bored: int = 0
    idx: int = 0

    while idx < len(segments):
        fragment = segments[idx]
        if fragment.startswith('I '):
            total_bored += 1
        idx += 1

    return total_bored