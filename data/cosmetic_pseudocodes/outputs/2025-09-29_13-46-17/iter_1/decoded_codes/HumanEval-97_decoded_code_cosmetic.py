def multiply(integer_a: int, integer_b: int) -> int:
    last_digit_a = integer_a % 10
    last_digit_b = integer_b % 10
    positive_last_digit_a = -last_digit_a if last_digit_a < 0 else last_digit_a
    positive_last_digit_b = -last_digit_b if last_digit_b < 0 else last_digit_b
    return positive_last_digit_a * positive_last_digit_b