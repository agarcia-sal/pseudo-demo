from typing import Callable

def largest_prime_factor(m: int) -> int:
    def is_prime(p: int) -> bool:
        if p < 2:
            return False
        r = 2
        while r < p:
            if p % r == 0:
                return False
            r += 1
        return True

    max_factor = 1
    q = 2
    while q <= m:
        if m % q == 0:
            if is_prime(q) and q > max_factor:
                max_factor = q
        q += 1
    return max_factor