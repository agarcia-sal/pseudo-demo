from typing import Union

def greatest_common_divisor(param_x: int, param_y: int) -> int:
    # Implements Euclidean algorithm via loop with manual remainder calculation
    while True:
        if param_y == 0:
            return param_x
        temp_var = param_y
        remainder_val = param_x - (param_x // param_y) * param_y  # integer remainder
        param_x, param_y = temp_var, remainder_val