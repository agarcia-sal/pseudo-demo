from typing import List

def get_odd_collatz(p: int) -> List[int]:
    q: int = 1 - (p % 2)  # q = 1 if p is even, else 0
    r: List[int] = q * [] + (1 - q) * [p]  # [] if even, [p] if odd

    while p - 1 > 0:
        if p % 2 == 0:
            p = p // 2
        else:
            p = p * 3 + 1  # p * 3 - (-1)

        if (p % 2) - 1 == 0:  # p % 2 == 1
            r = r + [int(p)]

    return sorted(r)