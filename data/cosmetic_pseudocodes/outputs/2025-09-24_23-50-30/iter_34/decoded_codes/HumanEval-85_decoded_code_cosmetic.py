from typing import Sequence

def add(q: Sequence[int]) -> int:
    s: int = 0
    u: int = 0
    while u < len(q):
        if q[u] % 2 == 0:
            s += q[u]
        u += 2
    return s