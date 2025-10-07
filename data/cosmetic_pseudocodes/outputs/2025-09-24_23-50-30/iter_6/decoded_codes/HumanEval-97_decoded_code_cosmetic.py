def multiply(param_x: int, param_y: int) -> int:
    first_digit_abs = param_x - (param_x // 10) * 10
    if first_digit_abs < 0:
        first_digit_abs = -first_digit_abs

    second_digit_abs = param_y - (param_y // 10) * 10
    if second_digit_abs < 0:
        second_digit_abs = -second_digit_abs

    return first_digit_abs * second_digit_abs