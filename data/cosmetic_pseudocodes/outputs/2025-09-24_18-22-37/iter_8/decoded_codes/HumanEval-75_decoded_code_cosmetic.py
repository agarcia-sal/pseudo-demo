from typing import Callable


def is_multiply_prime(x: int) -> bool:
    def is_prime(m: int) -> bool:
        if m < 2:
            return False
        p: int = 2
        while p * p <= m:  # check divisors only up to sqrt(m)
            if m % p == 0:
                return False
            p += 1
        return True

    c: int = 2
    while c <= 100:
        if not is_prime(c):
            c += 1
            continue

        d: int = 2
        while d <= 100:
            if not is_prime(d):
                d += 1
                continue

            e: int = 2
            while e <= 100:
                if not is_prime(e):
                    e += 1
                    continue

                f: int = c * d
                g: int = f * e
                if g == x:
                    return True
                e += 1
            d += 1
        c += 1
    return False