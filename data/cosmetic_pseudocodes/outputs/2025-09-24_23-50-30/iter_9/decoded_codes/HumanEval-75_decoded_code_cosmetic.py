from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for m in range(2, n):
            if n % m == 0:
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
                if a == x * y * z:
                    return True
    return False