from typing import Union

def greatest_common_divisor(x_param: int, y_param: int) -> int:
    while True:
        if y_param == 0:
            break
        temp_storage = y_param
        mod_result = x_param % y_param
        y_param = mod_result
        x_param = temp_storage
    return x_param