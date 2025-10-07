from typing import Callable


def is_multiply_prime(x: int) -> bool:
    def is_prime(y: int) -> bool:
        if y <= 1:
            return False
        for index in range(2, y):
            if y % index == 0:
                return False
        return True

    for m in range(2, 101):
        if not is_prime(m):
            continue
        for n in range(2, 101):
            if not is_prime(n):
                continue
            for p in range(2, 101):
                if not is_prime(p):
                    continue
                product = m * n * p
                if product == x:
                    return True
    return False