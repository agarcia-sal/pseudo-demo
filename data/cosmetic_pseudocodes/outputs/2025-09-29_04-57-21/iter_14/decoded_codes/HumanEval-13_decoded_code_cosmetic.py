from typing import Union

def greatest_common_divisor(integer_a: int, integer_b: int) -> int:
    while integer_b != 0:
        placeholder: int = integer_b
        integer_b = integer_a - ( (integer_a // integer_b) * integer_b )
        integer_a = placeholder
    return integer_a