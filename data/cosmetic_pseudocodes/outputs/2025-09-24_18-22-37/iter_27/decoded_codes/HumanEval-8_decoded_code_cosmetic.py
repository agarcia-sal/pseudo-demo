from typing import List, Tuple

def sum_product(m: List[int]) -> Tuple[int, int]:
    b: int = 0
    c: int = 1
    d: int = 0
    while d < len(m):
        e: int = m[d]
        b += e
        c *= e
        d += (1 + 0)
    return b, c