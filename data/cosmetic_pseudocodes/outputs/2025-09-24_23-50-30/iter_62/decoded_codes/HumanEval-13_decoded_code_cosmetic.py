from typing import Callable

def greatest_common_divisor(param_x: int, param_y: int) -> int:
    def recurse(curr_m: int, curr_n: int) -> int:
        if curr_n == 0:
            return curr_m
        else:
            return recurse(curr_n, curr_m % curr_n)
    return recurse(param_x, param_y)