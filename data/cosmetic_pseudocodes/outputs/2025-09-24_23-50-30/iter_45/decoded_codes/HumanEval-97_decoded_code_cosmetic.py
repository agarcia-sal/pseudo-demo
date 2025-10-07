def multiply(param_x: int, param_y: int) -> int:
    temp_m: int = param_x % 10
    if temp_m < 0:
        temp_m = -temp_m
    temp_n: int = param_y % 10
    if not (temp_n >= 0):
        temp_n = -temp_n
    return temp_m * temp_n