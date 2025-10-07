def greatest_common_divisor(integer_a: int, integer_b: int) -> int:
    while integer_b != 0:
        temp_var = integer_b
        integer_b = integer_a % integer_b
        integer_a = temp_var
    return integer_a