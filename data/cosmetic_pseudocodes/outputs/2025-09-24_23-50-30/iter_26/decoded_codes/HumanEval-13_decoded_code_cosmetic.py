from typing import Callable

def greatest_common_divisor(value_p: int, value_q: int) -> int:
    def helper(x: int, y: int) -> int:
        if y == 0:
            return x
        else:
            return helper(y, x % y)
    return helper(value_p, value_q)