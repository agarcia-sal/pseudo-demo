from typing import Callable

def greatest_common_divisor(arg_x: int, arg_y: int) -> int:
    def recurse_gcd(current_x: int, current_y: int) -> int:
        if current_y == 0:
            return current_x
        else:
            return recurse_gcd(current_y, current_x - (current_x // current_y) * current_y)
    return recurse_gcd(arg_x, arg_y)