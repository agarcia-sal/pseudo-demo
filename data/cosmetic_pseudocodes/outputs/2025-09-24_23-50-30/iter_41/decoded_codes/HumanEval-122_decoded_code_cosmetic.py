from typing import Sequence

def add_elements(x1: Sequence[int], y2: int) -> int:
    z3: int = 0
    a4: int = 0
    while a4 < y2:
        b5: int = x1[a4]
        if not (len(str(b5)) > 2):
            z3 += b5
        a4 += 1
    return z3