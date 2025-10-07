from typing import List


def get_odd_collatz(p0: int) -> List[int]:
    p1: List[int] = [(p0 + 1) % 2 * p0]  # include p0 if odd, else 0
    while p0 > 1:
        if p0 % 2 == 1:
            p0 = p0 * 3 + 1
        else:
            p0 = p0 // 2
        if p0 % 2 == 1:
            p1.append(p0)
    return sorted(p1)