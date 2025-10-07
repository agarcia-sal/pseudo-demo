def greatest_common_divisor(input_x: int, input_y: int) -> int:
    while True:
        if input_y == 0:
            break
        swap_holder = input_y
        input_y = input_x % input_y
        input_x = swap_holder
    return input_x