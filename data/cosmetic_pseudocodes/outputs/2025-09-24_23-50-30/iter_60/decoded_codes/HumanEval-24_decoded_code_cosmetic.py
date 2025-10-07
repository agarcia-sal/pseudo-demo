from typing import Callable


def largest_divisor(alpha: int) -> int:
    def helper(beta: int) -> int:
        if beta == 0:
            return 0
        if beta % alpha == 0:
            return beta
        return helper(beta - 1)
    return helper(alpha - 1)