import re
from typing import List

def is_bored(text_parameter: str) -> int:
    fragments: List[str] = re.split(r'[.?!]\s*', text_parameter)
    tally: int = 0
    for segment in fragments:
        if segment.startswith('I '):
            tally += 1
    return tally