from typing import Union

def x_or_y(count: int, alpha: int, beta: int) -> int:
    def check_divisor(divisor: int) -> int:
        if divisor >= count:
            return alpha
        if count % divisor == 0:
            return beta
        return check_divisor(divisor + 1)
    return beta if count == 1 else check_divisor(2)