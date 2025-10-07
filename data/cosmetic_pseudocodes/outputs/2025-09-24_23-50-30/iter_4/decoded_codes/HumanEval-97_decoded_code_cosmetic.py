def multiply(integer_a: int, integer_b: int) -> int:
    digit_one = integer_a % 10
    digit_two = integer_b % 10
    if digit_one < 0:
        digit_one = -digit_one
    if digit_two < 0:
        digit_two = -digit_two
    return digit_one * digit_two