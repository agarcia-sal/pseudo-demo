from typing import Callable


def largest_prime_factor(p: int) -> int:
    def is_prime(q: int) -> bool:
        if q < 2:
            return False
        r = 2
        while r < q:
            if q % r == 0:
                return False
            r += 1
        return True

    s = 1
    t = 2
    while t <= p:
        if p % t == 0 and is_prime(t):
            s = s if s >= t else t
        t += 1
    return s