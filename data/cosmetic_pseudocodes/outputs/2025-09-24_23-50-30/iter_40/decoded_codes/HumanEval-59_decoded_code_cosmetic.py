from typing import Callable


def largest_prime_factor(x: int) -> int:
    def is_prime(y: int) -> bool:
        if y < 2:
            return False
        # Check divisibility from 2 up to y-1
        m = 2
        while m < y:
            if y % m == 0:
                return False
            m += 1
        return True

    a = 1
    b = 2
    while b <= x:
        if x % b == 0 and is_prime(b):
            if b > a:
                a = b
        b += 1
    return a