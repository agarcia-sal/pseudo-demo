from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(x: int) -> bool:
        if x < 2:
            return False
        for divisor in range(2, x):
            if x % divisor == 0:
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
                if m * n * p == a:
                    return True

    return False