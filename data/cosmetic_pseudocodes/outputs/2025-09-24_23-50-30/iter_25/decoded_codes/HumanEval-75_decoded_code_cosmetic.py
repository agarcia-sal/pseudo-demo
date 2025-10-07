from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(m: int) -> bool:
        if m < 2:
            return False
        for r in range(2, m):
            if m % r == 0:
                return False
        return True

    for x in range(2, 101):
        if is_prime(x):
            for y in range(2, 101):
                if is_prime(y):
                    for z in range(2, 101):
                        if is_prime(z):
                            if a == x * y * z:
                                return True
    return False