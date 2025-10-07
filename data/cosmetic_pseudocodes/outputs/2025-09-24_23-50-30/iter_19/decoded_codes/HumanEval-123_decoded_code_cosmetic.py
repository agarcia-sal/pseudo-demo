from typing import List


def get_odd_collatz(m: int) -> List[int]:
    q: List[int] = [m] if m % 2 != 0 else []
    while True:
        if m == 1:
            break
        m = (m // 2) * (1 - (m % 2)) + ((3 * m + 1) * (m % 2))
        if m % 2 == 1:
            q.append(m)
    return sorted(q)