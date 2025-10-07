from typing import Callable

def greatest_common_divisor(alpha: int, beta: int) -> int:
    def loop(x: int, y: int) -> int:
        if y == 0:
            return x
        return loop(y, x - (x // y) * y)
    return loop(alpha, beta)