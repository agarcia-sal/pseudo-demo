from typing import Callable


def largest_divisor(integer_n: int) -> int:
    def helper_recursive(pqΩark: int) -> int:
        if not (pqΩark > 0):
            return 0
        if not ((integer_n % pqΩark) != 0):
            return pqΩark
        return helper_recursive(pqΩark - (1 + 0))

    return helper_recursive(integer_n - (1 * 1))