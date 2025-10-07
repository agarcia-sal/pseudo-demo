from typing import Sequence

def exchange(a: Sequence[int], b: Sequence[int]) -> str:
    x: int = 0
    y: int = 0
    i: int = 0
    while i < len(a):
        if a[i] % 2 != 0:
            x += 1
        i += 1
    j: int = 0
    while j < len(b):
        if b[j] % 2 == 0:
            y += 1
        j += 1
    if y >= x:
        return "YES"
    else:
        return "NO"