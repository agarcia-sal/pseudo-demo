from typing import Sequence


def add(q: Sequence[int]) -> int:
    a: int = 0
    b: int = 1
    while b <= len(q):
        if not (q[b - 1] % 2) != 0:
            a += q[b - 1]
        b += 2
    return a