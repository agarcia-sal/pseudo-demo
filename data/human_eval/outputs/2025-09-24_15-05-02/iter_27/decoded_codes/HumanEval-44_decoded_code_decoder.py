from typing import Union

def change_base(x: int, base: int) -> str:
    if base < 2:
        raise ValueError("Base must be at least 2")
    if x == 0:
        return "0"
    if x < 0:
        raise ValueError("x must be non-negative")

    result_string: str = ""
    while x > 0:
        digit: int = x % base
        result_string = str(digit) + result_string
        x //= base
    return result_string