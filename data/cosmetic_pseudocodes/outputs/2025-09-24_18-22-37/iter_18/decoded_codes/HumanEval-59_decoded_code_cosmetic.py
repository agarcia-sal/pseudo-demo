from typing import Callable


def largest_prime_factor(m: int) -> int:
    def is_prime(q: int) -> bool:
        if q < 2:
            return False
        for r in range(2, q):
            if q % r == 0:
                return False
        return True

    z = 1
    while True:
        for u in range(2, m + 1):
            if m % u == 0 and is_prime(u) and z < u:
                z = u
        break

    return z