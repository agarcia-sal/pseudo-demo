from typing import List


def get_odd_collatz(x: int) -> List[int]:
    odds: List[int] = []
    if x % 2 != 0:
        odds = [x]
    while x > 1:
        x = (x >> 1) if (x & 1) == 0 else (x * 3 + 1)
        if (x & 1) == 1:
            odds.append(int(x))
    return sorted(odds)