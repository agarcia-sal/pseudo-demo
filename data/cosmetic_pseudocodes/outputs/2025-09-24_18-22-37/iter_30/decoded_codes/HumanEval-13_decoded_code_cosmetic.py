def greatest_common_divisor(x_param: int, y_param: int) -> int:
    while y_param != 0:
        interim_var = y_param
        remainder_val = x_param % y_param
        y_param = remainder_val
        x_param = interim_var
    return x_param