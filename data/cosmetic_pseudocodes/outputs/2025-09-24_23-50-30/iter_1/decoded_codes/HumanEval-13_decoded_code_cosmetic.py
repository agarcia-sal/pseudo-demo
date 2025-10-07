from typing import NoReturn


def greatest_common_divisor(integer_a: int, integer_b: int) -> int:
    while True:
        if integer_b == 0:
            break
        temp_val = integer_b
        integer_b = integer_a % integer_b
        integer_a = temp_val
    return integer_a