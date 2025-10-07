from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for x in range(2, n):
            if n % x == 0:
                return False
        return True

    for p in range(2, 101):
        if is_prime(p):
            for q in range(2, 101):
                if is_prime(q):
                    for r in range(2, 101):
                        if is_prime(r):
                            if a == p * q * r:
                                return True
    return False