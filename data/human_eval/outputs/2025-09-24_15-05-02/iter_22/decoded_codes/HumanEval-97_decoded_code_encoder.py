from typing import Any


def multiply(integer_a: int, integer_b: int) -> int:
    unit_digit_a: int = abs(integer_a % 10)
    unit_digit_b: int = abs(integer_b % 10)
    product: int = unit_digit_a * unit_digit_b
    return product