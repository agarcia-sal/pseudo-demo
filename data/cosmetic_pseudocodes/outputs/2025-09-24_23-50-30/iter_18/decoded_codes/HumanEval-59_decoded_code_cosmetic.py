from typing import Callable


def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        if k <= 1:
            return False
        for u in range(2, k):
            if (k // u) * u == k:
                return False
        return True

    p = 1
    q = 2

    while q <= n:
        if (n // q) * q == n:
            if is_prime(q):
                if q > p:
                    p = q
        q += 1
    return p