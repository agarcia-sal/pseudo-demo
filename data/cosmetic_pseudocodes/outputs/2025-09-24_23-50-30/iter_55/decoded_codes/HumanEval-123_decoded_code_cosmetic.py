from typing import List


def get_odd_collatz(p: int) -> List[int]:
    q: List[int] = [] if p % 2 == 0 else [p]

    while p > 1:
        r = p % 2
        if r == 0:
            p //= 2
        else:
            p = 3 * p + 1

        if p % 2 == 1:
            q.append(p)

    return sorted(q)