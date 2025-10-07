def multiply(integer_a: int, integer_b: int) -> int:
    digit_one = abs(integer_a % 10)
    digit_two = abs(integer_b % 10)
    return digit_one * digit_two