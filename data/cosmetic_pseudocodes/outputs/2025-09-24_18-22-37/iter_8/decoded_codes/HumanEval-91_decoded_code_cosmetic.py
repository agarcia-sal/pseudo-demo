import re
from typing import List

def is_bored(human_input: str) -> int:
    fragments: List[str] = re.split(r'[.?!]\s*', human_input)
    tally: int = 0
    idx: int = 0
    while idx < len(fragments):
        current_piece: str = fragments[idx]
        snippet: str = current_piece[:2]
        if snippet == 'I ':
            tally += 1
        idx += 1
    return tally