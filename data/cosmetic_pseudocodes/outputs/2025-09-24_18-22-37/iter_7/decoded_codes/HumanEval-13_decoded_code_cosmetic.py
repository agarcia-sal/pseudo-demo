def greatest_common_divisor(value_x: int, value_y: int) -> int:
    while value_y != 0:
        temp_var = value_y
        remainder = value_x % value_y
        value_x = temp_var
        value_y = remainder
    return value_x