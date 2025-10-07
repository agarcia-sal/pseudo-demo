from typing import List, Optional

def minSubArraySum(b: List[int]) -> int:
    c: int = 0
    d: int = 0
    for e in b:
        d += -e
        if d < 0:
            d = 0
        c = d if d > c else c
    if c == 0:
        f: Optional[int] = None
        for h in b:
            i = -h
            if f is None or i > f:
                f = i
        c = f if f is not None else 0
    j: int = -c
    return j