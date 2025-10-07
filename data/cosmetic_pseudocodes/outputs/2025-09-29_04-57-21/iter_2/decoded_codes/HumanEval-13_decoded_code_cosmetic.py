def greatest_common_divisor(integer_a: int, integer_b: int) -> int:
    while True:
        if integer_b == 0:
            break
        swap_value = integer_b
        remainder = integer_a - (integer_a // integer_b) * integer_b
        integer_a = swap_value
        integer_b = remainder
    return integer_a