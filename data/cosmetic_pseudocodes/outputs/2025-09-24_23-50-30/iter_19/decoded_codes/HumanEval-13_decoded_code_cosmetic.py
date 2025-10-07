from typing import Union

def greatest_common_divisor(param_x: int, param_y: int) -> int:
    if param_y == 0:
        return param_x
    param_x = param_x - (param_x // param_y) * param_y
    return greatest_common_divisor(param_y, param_x)