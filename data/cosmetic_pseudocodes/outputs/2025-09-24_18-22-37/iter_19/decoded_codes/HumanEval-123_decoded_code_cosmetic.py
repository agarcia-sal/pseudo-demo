from typing import List

def get_odd_collatz(p: int) -> List[int]:
    q: List[int]
    if p % 2 != 1:
        q = []
    else:
        q = [p]

    while True:
        if p <= 1:
            break

        if p % 2 == 0:
            p = p // 2  # integer division
        else:
            p = 3 * p + 1

        if p % 2 == 1:
            q.append(int(p))

    s = sorted(q)
    return s