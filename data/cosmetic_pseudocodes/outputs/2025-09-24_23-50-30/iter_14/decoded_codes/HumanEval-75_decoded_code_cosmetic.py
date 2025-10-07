from typing import Callable


def is_multiply_prime(z: int) -> bool:
    def is_prime(m: int) -> bool:
        if m < 2:
            return False
        for x in range(2, m):
            if m % x == 0:
                return False
        return True

    for p in range(2, 101):
        if not is_prime(p):
            continue
        for q in range(2, 101):
            if not is_prime(q):
                continue
            for r in range(2, 101):
                if is_prime(r) and p * q * r == z:
                    return True
    return False