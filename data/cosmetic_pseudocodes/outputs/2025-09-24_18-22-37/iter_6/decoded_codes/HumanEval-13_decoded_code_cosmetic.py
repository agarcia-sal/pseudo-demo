from typing import Union

def greatest_common_divisor(x_param: int, y_param: int) -> int:
    while True:
        if y_param == 0:
            return x_param
        swap_temp = y_param
        remainder_calc = x_param - (x_param // y_param) * y_param
        y_param = remainder_calc
        x_param = swap_temp
        if y_param == 0:
            return x_param