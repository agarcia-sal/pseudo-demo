import re
from typing import List

def is_bored(input_string: str) -> int:
    fragments: List[str] = re.split(r'[.?!]\s*', input_string)
    tally: int = 0
    idx: int = 0
    while idx < len(fragments):
        # Check if the fragment starts with 'I ' (exactly 'I ' at the beginning)
        if not fragments[idx].startswith('I '):
            idx += 1
            continue
        tally += 1
        idx += 1
    return tally