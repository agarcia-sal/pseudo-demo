def greatest_common_divisor(param_x: int, param_y: int) -> int:
    while True:
        if param_y == 0:
            break
        temp_var = param_y
        param_y = param_x % param_y
        param_x = temp_var
    return param_x