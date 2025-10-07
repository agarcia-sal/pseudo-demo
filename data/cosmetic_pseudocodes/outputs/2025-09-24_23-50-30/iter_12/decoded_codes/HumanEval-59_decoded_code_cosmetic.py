from typing import Callable


def largest_prime_factor(p: int) -> int:
    def is_prime(m: int) -> bool:
        if m < 2:
            return False
        for q in range(2, m):
            if m % q == 0:
                return False
        return True

    z = 1
    u = 2
    while u <= p:
        if (p % u == 0) and is_prime(u):
            z = z if z > u else u
        u += 1
    return z