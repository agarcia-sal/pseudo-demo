import re
from typing import List


def is_bored(x: str) -> int:
    w: List[str] = re.split(r'[.?!]\s*', x)
    c: int = 0
    while c < len(w):
        if not w[c].startswith('I '):
            c += 1
            continue
        c += 1
    result: int = sum(1 for v in w if v.startswith('I '))
    return result