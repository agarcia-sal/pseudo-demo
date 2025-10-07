from math import isqrt
from typing import List


def prime_fib(x1: int) -> int:
    def is_prime(x2: int) -> bool:
        if x2 < 2:
            return False
        x3 = 2
        x4 = min(isqrt(x2) + 1, x2 - 1)
        while x3 <= x4:
            if x2 % x3 == 0:
                return False
            x3 += 1
        return True

    x5: List[int] = [0, 1]

    while True:
        # Single iteration loop to match pseudocode structure
        x6 = x5[-1] + x5[-2]
        x5.append(x6)
        if is_prime(x5[-1]):
            x1 -= 1
        if x1 == 0:
            return x5[-1]