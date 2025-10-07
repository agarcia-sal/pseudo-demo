def multiply(a, b):
    unit_digit_a = abs(a) % 10
    unit_digit_b = abs(b) % 10
    result = unit_digit_a * unit_digit_b
    return result