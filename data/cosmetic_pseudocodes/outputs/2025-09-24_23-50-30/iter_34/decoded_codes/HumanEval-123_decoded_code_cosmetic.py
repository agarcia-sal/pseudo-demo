from typing import List, Set


def get_odd_collatz(m: int) -> List[int]:
    q: Set[int] = {m} if m % 2 == 1 else set()

    while m > 1:
        m = m // 2 if m % 2 == 0 else m * 3 + 1
        if m % 2 == 1:
            q.add(m)

    return sorted(q)