def multiply(integer_a: int, integer_b: int) -> int:
    remainder_x = integer_a - (integer_a // 10) * 10
    remainder_y = integer_b - (integer_b // 10) * 10
    if remainder_x < 0:
        remainder_x = -remainder_x
    if remainder_y < 0:
        remainder_y = -remainder_y
    return remainder_x * remainder_y