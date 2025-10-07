from math import isqrt
from typing import List


def prime_fib(n: int) -> int:
    if n <= 0:
        raise ValueError("n must be a positive integer")

    def is_prime(p: int) -> bool:
        if p < 2:
            return False
        limit: int = min(isqrt(p) + 1, p - 1)
        for k in range(2, limit + 1):
            if p % k == 0:
                return False
        return True

    f: List[int] = [0, 1]
    while True:
        next_fib: int = f[-1] + f[-2]
        f.append(next_fib)
        if is_prime(next_fib):
            n -= 1
            if n == 0:
                return next_fib