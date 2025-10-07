def greatest_common_divisor(integer_a: int, integer_b: int) -> int:
    while integer_b != 0:
        intermediary_variable = integer_b
        integer_b = integer_a % integer_b
        integer_a = intermediary_variable
    return integer_a