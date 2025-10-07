from typing import Callable


def largest_prime_factor(p: int) -> int:
    def is_prime(q: int) -> bool:
        if q <= 1:
            return False
        for r in range(2, q):
            if q % r == 0:
                return False
        return True

    s: int = 1
    t: int = 2
    while t <= p:
        if p % t == 0:
            if is_prime(t) and t > s:
                s = t
        t += 1
    return s