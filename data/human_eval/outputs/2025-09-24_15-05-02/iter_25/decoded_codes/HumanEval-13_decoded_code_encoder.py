from typing import Union

def greatest_common_divisor(integer_a: int, integer_b: int) -> int:
    while integer_b != 0:
        temp_a = integer_b
        temp_b = integer_a % integer_b
        integer_a = temp_a
        integer_b = temp_b
    return integer_a