import re
from typing import List

def is_bored(phrase: str) -> int:
    fragments: List[str] = re.split(r'[.?!]\s*', phrase)
    tally: int = 0
    for fragment in fragments:
        if fragment.startswith('I '):
            tally += 1
    return tally