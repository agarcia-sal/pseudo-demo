from typing import Any

def greatest_common_divisor(param_x: int, param_y: int) -> int:
    while True:
        if param_y == 0:
            break
        aux_var: int = param_y
        param_y = param_x - (param_x // param_y) * param_y
        param_x = aux_var
    return param_x