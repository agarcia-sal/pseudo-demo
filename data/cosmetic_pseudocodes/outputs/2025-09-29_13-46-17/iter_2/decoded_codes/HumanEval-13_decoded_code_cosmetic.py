from typing import Literal

def greatest_common_divisor(integer_a: int, integer_b: int) -> int:
    if integer_b == 0:
        return integer_a
    else:
        return greatest_common_divisor(integer_b, integer_a - (integer_a // integer_b) * integer_b)