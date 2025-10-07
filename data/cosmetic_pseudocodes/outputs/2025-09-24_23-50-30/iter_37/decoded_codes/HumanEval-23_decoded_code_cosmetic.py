from typing import Sequence

def strlen(s: Sequence) -> int:
    c: int = 0
    while c < len(s):
        c += 1
    return c