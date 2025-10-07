from typing import Callable


def greatest_common_divisor(integer_a: int, integer_b: int) -> int:
    def recursive_helper(x: int, y: int) -> int:
        if y == 0:
            return x
        return recursive_helper(y, x - (x // y) * y)

    return recursive_helper(integer_a, integer_b)