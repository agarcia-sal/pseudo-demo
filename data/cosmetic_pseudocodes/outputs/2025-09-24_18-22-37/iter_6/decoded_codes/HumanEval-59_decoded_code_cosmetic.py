from typing import Callable


def largest_prime_factor(p: int) -> int:
    def is_prime(q: int) -> bool:
        if q < 2:
            return False
        for u in range(2, q):
            if q % u == 0:
                return False
        return True

    r: int = 1
    v: int = 2
    while v <= p:
        if p % v != 0:
            v += 1
            continue
        if is_prime(v):
            if r < v:
                r = v
        v += 1

    return r