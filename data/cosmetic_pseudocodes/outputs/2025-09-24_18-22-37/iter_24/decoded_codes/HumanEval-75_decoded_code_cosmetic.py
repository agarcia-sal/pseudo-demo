from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        if n < 2:
            return False  # 0 and 1 are not prime
        for s in range(2, n):
            if n % s == 0:
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
                if x * y * z == a:
                    return True
    return False