from typing import Callable


def largest_prime_factor(m: int) -> int:
    def is_prime(q: int) -> bool:
        if q < 2:
            return False

        def check_divisor(r: int, s: int) -> bool:
            if s == r:
                return True
            if q % s == 0:
                return False
            return check_divisor(r, s + 1)

        return check_divisor(q, 2)

    e: int = 1
    u: int = 2
    while u <= m:
        if m % u == 0 and is_prime(u):
            if e < u:
                e = u
        u += 1
    return e