def greatest_common_divisor(number_x: int, number_y: int) -> int:
    while True:
        if number_y == 0:
            break
        helper_var = number_y
        remainder_val = number_x % number_y
        number_y = remainder_val
        number_x = helper_var
    return number_x