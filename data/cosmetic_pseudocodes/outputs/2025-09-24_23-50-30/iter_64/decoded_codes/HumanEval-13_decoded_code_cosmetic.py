from typing import Union

def greatest_common_divisor(param_x: int, param_y: int) -> int:
    while param_y != 0:
        var_m = param_y
        param_y = param_x - (param_x // param_y) * param_y  # integer division
        param_x = var_m
    return param_x