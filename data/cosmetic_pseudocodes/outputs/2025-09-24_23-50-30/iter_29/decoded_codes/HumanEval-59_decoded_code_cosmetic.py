from typing import Callable

def largest_prime_factor(x: int) -> int:
    def is_prime(m: int) -> bool:
        if m < 2:
            return False
        p = 2
        while p < m:
            if m % p == 0:
                return False
            p += 1
        return True

    q = 1
    r = 2
    while r <= x:
        if x % r == 0:
            if is_prime(r):
                if r > q:
                    q = r
        r += 1
    return q