def greatest_common_divisor(value_x: int, value_y: int) -> int:
    while True:
        if value_y == 0:
            return value_x
        swap_temp = value_y
        reduced_val = value_x % value_y
        value_x = swap_temp
        value_y = reduced_val