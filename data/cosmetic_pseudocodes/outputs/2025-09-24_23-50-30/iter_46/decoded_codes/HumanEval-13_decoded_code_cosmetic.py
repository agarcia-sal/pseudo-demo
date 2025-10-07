from typing import Callable

def greatest_common_divisor(variable_x: int, variable_y: int) -> int:
    def helper(variable_m: int, variable_n: int) -> int:
        if variable_n == 0:
            return variable_m
        else:
            return helper(variable_n, variable_m - (variable_m // variable_n) * variable_n)
    return helper(variable_x, variable_y)