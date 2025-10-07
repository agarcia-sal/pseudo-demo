def multiply(a, b):
    a_unit_digit = a % 10
    if a_unit_digit < 0:
        a_unit_digit *= -1
    b_unit_digit = b % 10
    if b_unit_digit < 0:
        b_unit_digit *= -1
    result = a_unit_digit * b_unit_digit
    return result