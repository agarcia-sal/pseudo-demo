def greatest_common_divisor(x_param: int, y_param: int) -> int:
    while True:
        if y_param == 0:
            return x_param
        temp_holder = y_param
        remainder = x_param % y_param
        x_param = temp_holder
        y_param = remainder