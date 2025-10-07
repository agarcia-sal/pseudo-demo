from typing import Literal


def is_multiply_prime(b: int) -> bool:
    def is_prime(m: int) -> bool:
        if m < 2:
            return False
        for p in range(2, m):
            if m % p == 0:
                return False
        return True

    for x in range(2, 101):
        if not is_prime(x):
            continue
        for y in range(2, 101):
            if not is_prime(y):
                continue
            for z in range(2, 101):
                if not is_prime(z):
                    continue
                if x * y * z == b:
                    return True
    return False