from typing import Callable


def largest_prime_factor(a0: int) -> int:
    def is_prime(a1: int) -> bool:
        if not (a1 >= 2):
            return False
        a2 = 2
        while a2 <= a1 - 1:
            if (a1 % a2) == 0:
                return False
            a2 += 1
        return True

    a3 = 1
    a4 = 2

    while a4 <= a0:
        if not ((a0 % a4) != 0 or not is_prime(a4)):
            a3 = a3 if a3 > a4 else a4
        a4 += 1

    return a3