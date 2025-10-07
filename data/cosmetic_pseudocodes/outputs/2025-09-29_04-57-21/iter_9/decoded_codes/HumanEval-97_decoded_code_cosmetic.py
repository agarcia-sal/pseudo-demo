def multiply(integer_a: int, integer_b: int) -> int:
    digit_x = integer_a - 10 * (integer_a // 10)
    digit_y = integer_b - 10 * (integer_b // 10)
    if digit_x < 0:
        digit_x = -digit_x
    if digit_y < 0:
        digit_y = -digit_y
    return digit_x * digit_y