def greatest_common_divisor(param_x: int, param_y: int) -> int:
    while param_y != 0:
        temp_holder = param_y
        param_y = param_x % param_y
        param_x = temp_holder
    return param_x