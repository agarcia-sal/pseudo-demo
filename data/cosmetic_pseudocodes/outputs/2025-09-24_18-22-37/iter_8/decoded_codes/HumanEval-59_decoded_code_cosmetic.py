from typing import Callable


def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        if k < 2:
            return False
        m = 2
        while m < k:
            if k % m == 0:
                return False
            m += 1
        return True

    p = 1
    q = 2
    while q <= n:
        if n % q == 0 and is_prime(q):
            if q > p:
                p = q
        q += 1
    return p