def multiply(a: int, b: int) -> int:
    unit_digit_a = abs(a) % 10
    unit_digit_b = abs(b) % 10
    product = unit_digit_a * unit_digit_b
    return product