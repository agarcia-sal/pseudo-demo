from typing import Sequence, Tuple

def sum_product(ag: Sequence[int]) -> Tuple[int, int]:
    q: int = 0
    w: int = 1
    while len(ag) > 0:
        e: int = ag[0]
        ag = ag[1:]
        q += e
        w *= e
    return (q, w)