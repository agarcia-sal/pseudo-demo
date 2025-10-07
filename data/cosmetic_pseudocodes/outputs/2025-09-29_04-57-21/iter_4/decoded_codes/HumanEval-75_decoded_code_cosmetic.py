from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for divisor in range(2, num):
            if num % divisor == 0:
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