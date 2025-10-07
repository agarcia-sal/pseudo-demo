from typing import List

def get_odd_collatz(p: int) -> List[int]:
    r: List[int]
    if p % 2 != 0:
        r = [p]
    else:
        r = []

    while p > 1:
        if p % 2 == 0:
            p //= 2
        else:
            p = p * 3 + 1

        if p % 2 == 1:
            r.append(int(p))

    u: List[int] = sorted(r)
    return u