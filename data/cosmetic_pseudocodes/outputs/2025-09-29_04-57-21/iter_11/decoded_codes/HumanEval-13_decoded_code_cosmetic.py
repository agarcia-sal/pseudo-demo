def greatest_common_divisor(input_x: int, input_y: int) -> int:
    while input_y != 0:
        swap_temp = input_y
        input_y = input_x % input_y
        input_x = swap_temp
    return input_x