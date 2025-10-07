def greatest_common_divisor(input_x: int, input_y: int) -> int:
    while True:
        if input_y == 0:
            return input_x
        swap_holder = input_y
        remainder_val = input_x % input_y
        input_x = swap_holder
        input_y = remainder_val