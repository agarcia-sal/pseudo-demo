from typing import List


def get_odd_collatz(p: int) -> List[int]:
    r: List[int]
    if p % 2 != 1:
        r = []
    else:
        r = [p]

    while p > 1:
        if p % 2 == 0:
            p = p // 2
        else:
            p = p * 3 + 1

        if p % 2 == 1:
            q = int(p)
            r.append(q)

    return sorted(r)