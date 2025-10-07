from typing import Union

def greatest_common_divisor(integer_a: int, integer_b: int) -> int:
    a, b = abs(integer_a), abs(integer_b)  # Handle negative inputs robustly
    while b != 0:
        a, b = b, a % b
    return a