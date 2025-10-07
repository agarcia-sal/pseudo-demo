import math
from typing import List

def prime_fib(n: int) -> int:
    def is_prime(p: int) -> bool:
        if p < 2:
            return False
        limit = min(int(math.sqrt(p)) + 1, p - 1)
        for k in range(2, limit):
            if p % k == 0:
                return False
        return True

    f: List[int] = [0, 1]
    while True:
        new_fib = f[-1] + f[-2]
        f.append(new_fib)
        if is_prime(new_fib):
            n -= 1
        if n == 0:
            return new_fib