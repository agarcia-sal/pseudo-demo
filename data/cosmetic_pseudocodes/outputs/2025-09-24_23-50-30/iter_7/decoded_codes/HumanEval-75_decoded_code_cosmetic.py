from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(x: int) -> bool:
        if x < 2:
            return False
        for u in range(2, x):
            if x % u == 0:
                return False
        return True

    for m in range(2, 101):
        if is_prime(m):
            for n in range(2, 101):
                if is_prime(n):
                    for p in range(2, 101):
                        if is_prime(p):
                            if a == m * n * p:
                                return True
    return False