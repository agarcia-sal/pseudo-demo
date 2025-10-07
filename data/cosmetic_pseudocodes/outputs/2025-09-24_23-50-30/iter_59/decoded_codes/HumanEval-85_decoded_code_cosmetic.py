from typing import Sequence

def add(a: Sequence[int]) -> int:
    b: int = 0
    c: int = 1
    while c <= len(a):
        if (a[c - 1] % 2) == 0:
            b += a[c - 1]
            # continue immediately to next iteration as per pseudocode
        # else case does nothing, continue anyway
        c += 2
    return b