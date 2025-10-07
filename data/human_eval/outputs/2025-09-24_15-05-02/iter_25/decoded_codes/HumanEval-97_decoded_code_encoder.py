from typing import Union

def multiply(a: int, b: int) -> int:
    unit_digit_a: int = abs(a) % 10
    unit_digit_b: int = abs(b) % 10
    return unit_digit_a * unit_digit_b