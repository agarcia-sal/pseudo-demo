from math import isqrt
from typing import List

def prime_fib(n: int) -> int:
    def is_prime(p: int) -> bool:
        if p < 2:
            return False
        limit = min(isqrt(p) + 1, p)
        for k in range(2, limit):
            if p % k == 0:
                return False
        return True

    f: List[int] = [0, 1]
    while True:
        next_fib = f[-1] + f[-2]
        f.append(next_fib)
        if is_prime(next_fib):
            n -= 1
            if n == 0:
                return next_fib