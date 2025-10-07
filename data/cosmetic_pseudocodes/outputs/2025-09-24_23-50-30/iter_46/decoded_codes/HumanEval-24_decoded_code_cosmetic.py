from typing import Callable


def largest_divisor(integer_n: int) -> int:
    def helper_recursion(integer_j: int) -> int:
        if integer_j > 0 and integer_n % integer_j == 0:
            return integer_j
        if integer_j > 0:
            return helper_recursion(integer_j - 1)
        return 0

    return helper_recursion(integer_n - 1)