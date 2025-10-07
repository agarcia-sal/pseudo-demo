from typing import Callable

def largest_prime_factor(x: int) -> int:
    def is_prime(y: int) -> bool:
        if y < 2:
            return False
        p = 2
        while p < y:
            if y % p == 0:
                return False
            p += 1
        return True

    greatest = 1
    q = 2
    while q <= x:
        if x % q == 0:
            if is_prime(q):
                if q > greatest:
                    greatest = q
        q += 1
    return greatest