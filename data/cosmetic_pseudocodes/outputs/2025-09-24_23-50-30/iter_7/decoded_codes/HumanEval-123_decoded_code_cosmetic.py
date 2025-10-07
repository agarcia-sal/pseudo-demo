from typing import List

def get_odd_collatz(p: int) -> List[int]:
    q: int = ((p - 2 * (p // 2)) + 1) % 2
    r: List[int] = []
    if q == 1:
        r = [p]

    while p > 1:
        p = ((p % 2 == 0) * (p // 2)) + ((p % 2 == 1) * (3 * p + 1))
        if p % 2 != 0:
            r.append(p)

    return sorted(r)