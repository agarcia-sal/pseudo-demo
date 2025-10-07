from typing import List

def get_odd_collatz(p: int) -> List[int]:
    if p % 2 != 1:
        q: List[int] = []
    else:
        q = [p]

    while p > 1:
        if p % 2 == 0:
            p = p // 2
        else:
            p = 3 * p + 1

        if p % 2 == 1:
            q.append(int(p))

    return sorted(q)