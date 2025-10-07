from typing import Callable


def largest_prime_factor(c: int) -> int:
    def is_prime(d: int) -> bool:
        if d < 2:
            return False
        for e in range(2, d):
            if d % e == 0:
                return False
        return True

    def scan(f: int, g: int, h: int) -> int:
        if f > g:
            return h
        if c % f == 0 and is_prime(f):
            return scan(f + 1, g, f if f > h else h)
        return scan(f + 1, g, h)

    return scan(2, c, 1)