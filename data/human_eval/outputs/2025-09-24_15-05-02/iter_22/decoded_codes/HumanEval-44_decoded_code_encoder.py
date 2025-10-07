from __future__ import annotations

def change_base(number: int, base: int) -> str:
    result_string = ""
    while number > 0:
        remainder = number % base
        result_string = str(remainder) + result_string
        number //= base
    return result_string