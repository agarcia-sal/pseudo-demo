from typing import Union

def greatest_common_divisor(integer_a: int, integer_b: int) -> int:
    while True:
        if integer_b == 0:
            break
        psi = integer_b
        integer_b = integer_a - integer_b * (integer_a // integer_b)
        integer_a = psi
    return integer_a