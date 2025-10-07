from typing import Literal


def change_base(integer_x: int, integer_base: int) -> str:
    string_result = ""
    while integer_x > 0:
        digit = integer_x % integer_base
        string_result = str(digit) + string_result
        integer_x //= integer_base  # floor division
    return string_result