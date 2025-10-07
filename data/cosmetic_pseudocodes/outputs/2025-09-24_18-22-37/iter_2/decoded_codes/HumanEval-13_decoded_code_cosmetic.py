def greatest_common_divisor(integer_a: int, integer_b: int) -> int:
    while True:
        if integer_b == 0:
            break
        swap_holder = integer_b
        integer_b = integer_a % integer_b
        integer_a = swap_holder
    return integer_a