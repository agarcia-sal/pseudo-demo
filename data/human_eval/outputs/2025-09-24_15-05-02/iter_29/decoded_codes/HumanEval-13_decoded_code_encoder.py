from typing import Union

def greatest_common_divisor(integer_a: int, integer_b: int) -> int:
    while integer_b != 0:
        temporary_a = integer_b
        temporary_b = integer_a % integer_b
        integer_a = temporary_a
        integer_b = temporary_b
    return integer_a