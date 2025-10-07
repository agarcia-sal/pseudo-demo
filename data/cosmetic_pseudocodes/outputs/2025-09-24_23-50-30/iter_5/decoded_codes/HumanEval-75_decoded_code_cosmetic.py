from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for idx in range(2, n):
            if n % idx == 0:
                return False
        return True

    for x in range(2, 101):
        if is_prime(x):
            for y in range(2, 101):
                if is_prime(y):
                    for z in range(2, 101):
                        if is_prime(z) and a == x * y * z:
                            return True
    return False