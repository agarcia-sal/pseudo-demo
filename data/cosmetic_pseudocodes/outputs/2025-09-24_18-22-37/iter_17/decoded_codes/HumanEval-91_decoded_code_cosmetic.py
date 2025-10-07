import re
from typing import List

def is_bored(alpha: str) -> int:
    parts: List[str] = re.split(r'[.?!]\s*', alpha)
    tally: int = 0
    idx: int = 0
    while idx < len(parts):
        snippet = parts[idx]
        if len(snippet) >= 2:
            prefix = snippet[:2]
            if prefix == 'I ':
                tally += 1
        idx += 1
    return tally