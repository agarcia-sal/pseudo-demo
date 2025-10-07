def multiply(param_x: int, param_y: int) -> int:
    temp_m = param_x % 10
    if temp_m < 0:
        temp_m = -temp_m

    temp_n = param_y % 10
    if temp_n < 0:
        temp_n = -temp_n

    return temp_m * temp_n