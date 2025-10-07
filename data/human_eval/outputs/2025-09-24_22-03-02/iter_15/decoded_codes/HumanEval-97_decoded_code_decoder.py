def multiply(a, b):
    first_unit_digit = abs(a % 10)
    second_unit_digit = abs(b % 10)
    product = first_unit_digit * second_unit_digit
    return product