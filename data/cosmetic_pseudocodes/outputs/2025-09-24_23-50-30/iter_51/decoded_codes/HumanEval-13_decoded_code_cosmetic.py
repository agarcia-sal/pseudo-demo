from typing import Callable

def greatest_common_divisor(q: int, w: int) -> int:
    def helper(x: int, y: int) -> int:
        if y == 0:
            return x
        else:
            return helper(y, x - (x // y) * y)
    return helper(q, w)