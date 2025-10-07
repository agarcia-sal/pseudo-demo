from typing import Callable


def largest_prime_factor(x: int) -> int:
    def is_prime(y: int) -> bool:
        if y < 2:
            return False
        for m in range(2, y):
            if y % m == 0:
                return False
        return True

    a = 1
    b = 2
    while b <= x:
        if x % b == 0 and is_prime(b):
            if a < b:
                a = b
        b += 1
    return a