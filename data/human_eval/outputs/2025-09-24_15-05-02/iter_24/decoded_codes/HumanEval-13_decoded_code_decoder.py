from typing import Union

def greatest_common_divisor(a: int, b: int) -> int:
    """Compute the greatest common divisor of two integers using the Euclidean algorithm."""
    while b != 0:
        temp_a = b
        b = a % b
        a = temp_a
    return a