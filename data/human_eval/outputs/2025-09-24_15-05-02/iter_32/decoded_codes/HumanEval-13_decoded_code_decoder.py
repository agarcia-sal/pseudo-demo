def greatest_common_divisor(integer_a: int, integer_b: int) -> int:
    while integer_b != 0:
        temporary_value = integer_b
        integer_b = integer_a % integer_b
        integer_a = temporary_value
    return integer_a