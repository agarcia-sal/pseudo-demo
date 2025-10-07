from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(x: int) -> bool:
        if x < 2:
            return False
        for m in range(2, x):
            if x % m == 0:
                return False
        return True

    for p in range(2, 101):
        if not is_prime(p):
            continue
        for q in range(2, 101):
            if not is_prime(q):
                continue
            for r in range(2, 101):
                if not is_prime(r):
                    continue
                if p * q * r == a:
                    return True
    return False