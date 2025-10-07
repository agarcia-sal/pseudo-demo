def multiply(a: int, b: int) -> int:
    remainder_a = a % 10
    absolute_remainder_a = abs(remainder_a)
    remainder_b = b % 10
    absolute_remainder_b = abs(remainder_b)
    product = absolute_remainder_a * absolute_remainder_b
    return product