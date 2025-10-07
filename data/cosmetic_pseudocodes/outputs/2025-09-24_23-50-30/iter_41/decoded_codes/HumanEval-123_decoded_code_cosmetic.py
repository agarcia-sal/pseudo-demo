from typing import List


def get_odd_collatz(p: int) -> List[int]:
    q: List[int] = [p] if p % 2 != 0 else []

    while p > 1:
        if p % 2 == 0:
            p //= 2
        else:
            p = p * 3 + 1
        if p % 2 != 0:
            q.append(int(p))

    return sorted(q)