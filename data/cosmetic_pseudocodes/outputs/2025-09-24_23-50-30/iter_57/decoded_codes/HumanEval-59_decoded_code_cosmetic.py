from typing import Callable


def largest_prime_factor(m: int) -> int:
    def is_prime(p: int) -> bool:
        if p < 2:
            return False
        for x in range(2, p):
            if p % x == 0:
                return False
        return True

    r: int = 1
    q: int = 2
    while q <= m:
        if m % q == 0 and is_prime(q):
            if r < q:
                r = q
        q += 1
    return r