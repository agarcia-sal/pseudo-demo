from typing import Callable


def is_multiply_prime(b: int) -> bool:
    def is_prime(c: int) -> bool:
        if c < 2:
            return False
        for d in range(2, c):
            if c % d == 0:
                return False
        return True

    for e in range(2, 101):
        if not is_prime(e):
            continue
        for f in range(2, 101):
            if not is_prime(f):
                continue
            for g in range(2, 101):
                if not is_prime(g):
                    continue
                if e * f * g == b:
                    return True
    return False