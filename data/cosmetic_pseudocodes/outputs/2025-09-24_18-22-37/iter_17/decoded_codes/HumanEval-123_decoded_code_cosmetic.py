from typing import List

def get_odd_collatz(p: int) -> List[int]:
    v: List[int]
    w: List[int]
    q: int

    if (p % 2) != 1:
        v = []
    else:
        v = [p]

    while p > 1:
        if (p % 2) == 0:
            p = p // 2
        else:
            p = (p * 3) + 1

        q = p % 2
        if q == 1:
            v.append(int(p))

    w = sorted(v)
    return w