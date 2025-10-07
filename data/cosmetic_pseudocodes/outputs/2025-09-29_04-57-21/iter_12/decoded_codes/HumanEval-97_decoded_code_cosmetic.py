def multiply(integer_a: int, integer_b: int) -> int:
    remainder_a = integer_a % 10
    if remainder_a < 0:
        remainder_a = -remainder_a

    remainder_b = integer_b % 10
    if remainder_b < 0:
        remainder_b = -remainder_b

    return remainder_a * remainder_b