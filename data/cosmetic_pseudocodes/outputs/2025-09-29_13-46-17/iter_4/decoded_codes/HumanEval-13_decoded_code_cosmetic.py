from typing import Callable

def greatest_common_divisor(alpha: int, beta: int) -> int:
    def gcd_helper(x: int, y: int) -> int:
        if y == 0:
            return x
        else:
            return gcd_helper(y, x - (x // y) * y)  # Use integer division for floor

    return gcd_helper(alpha, beta)