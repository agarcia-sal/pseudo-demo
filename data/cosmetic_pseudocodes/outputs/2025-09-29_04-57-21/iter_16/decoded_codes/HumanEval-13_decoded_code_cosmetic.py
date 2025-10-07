def greatest_common_divisor(integer_a: int, integer_b: int) -> int:
    while integer_b != 0:
        swap_holder = integer_b
        integer_b = integer_a - (integer_a // integer_b) * integer_b  # use integer division
        integer_a = swap_holder
    return integer_a