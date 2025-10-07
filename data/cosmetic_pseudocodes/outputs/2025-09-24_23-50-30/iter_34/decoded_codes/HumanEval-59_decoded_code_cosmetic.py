from typing import NoReturn


def largest_prime_factor(a: int) -> int:
    def is_prime(b: int) -> bool:
        if b < 2:
            return False
        for m in range(2, b):
            if b % m == 0:
                return False
        return True

    c: int = 1
    d: int = 2
    while d <= a:
        if a % d == 0 and is_prime(d):
            if d > c:
                c = d
        d += 1
    return c