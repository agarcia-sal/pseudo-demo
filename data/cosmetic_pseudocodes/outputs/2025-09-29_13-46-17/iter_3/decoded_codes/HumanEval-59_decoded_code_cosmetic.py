from typing import Callable


def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        if k < 2:
            return False

        def check_divisor(dividend: int, limit: int) -> bool:
            if dividend == limit:
                return True
            if limit % dividend == 0:
                return False
            return check_divisor(dividend + 1, limit)

        return check_divisor(2, k)

    def find_largest(divisor: int, limit: int, currentMax: int) -> int:
        if divisor > limit:
            return currentMax
        if limit % divisor == 0 and is_prime(divisor):
            if divisor > currentMax:
                currentMax = divisor
        return find_largest(divisor + 1, limit, currentMax)

    return find_largest(2, n, 1)