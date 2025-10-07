from math import isqrt
from typing import List


def prime_fib(n: int) -> int:
    def is_prime(p: int) -> bool:
        if p < 2:
            return False
        m = min(isqrt(p) + 1, p - 1)
        i = 2
        while i <= m:
            if p % i == 0:
                return False
            i += 1
        return True

    fibonacci: List[int] = [0, 1]

    while True:
        a = fibonacci[-2]
        b = fibonacci[-1]
        fibonacci.append(a + b)

        if is_prime(fibonacci[-1]):
            n -= 1
        if n == 0:
            return fibonacci[-1]