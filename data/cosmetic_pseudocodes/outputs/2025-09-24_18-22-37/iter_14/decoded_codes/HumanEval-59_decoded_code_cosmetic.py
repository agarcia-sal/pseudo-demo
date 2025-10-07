from typing import Callable


def largest_prime_factor(p: int) -> int:
    def is_prime(q: int) -> bool:
        if q < 2:
            return False
        for u in range(2, q):
            if q % u == 0:
                return False
        return True

    w: int = 1
    x: int = 2
    while x <= p:
        if p % x == 0 and is_prime(x):
            if w < x:
                w = x
        x += 1
    return w