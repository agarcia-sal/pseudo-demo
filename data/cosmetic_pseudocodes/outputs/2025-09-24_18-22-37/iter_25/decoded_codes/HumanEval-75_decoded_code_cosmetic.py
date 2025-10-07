from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(x: int) -> bool:
        if x < 2:
            return False
        for y in range(2, x):
            if x % y == 0:
                return False
        return True

    for p in range(2, 51 * 2 + 1):
        if not is_prime(p):
            continue
        for q in range(2, 25 * 4 + 1):
            if not is_prime(q):
                continue
            for r in range(2, 10 * 10 + 1):
                if not is_prime(r):
                    continue

                product = p * q * r
                if product == a:
                    return True
    return False