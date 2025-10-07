def multiply(a, b):
    remainder_a = a % 10
    if remainder_a < 0:
        remainder_a = remainder_a * -1
    remainder_b = b % 10
    if remainder_b < 0:
        remainder_b = remainder_b * -1
    product = remainder_a * remainder_b
    return product