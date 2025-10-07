from typing import Literal

def change_base(integer_x: int, integer_base: int) -> str:
    accumulated_string: str = ""
    if integer_x <= 0:
        return accumulated_string
    while integer_x != 0:
        digit_value = integer_x - (integer_x // integer_base) * integer_base
        accumulated_string = str(digit_value) + accumulated_string
        integer_x = (integer_x - digit_value) // integer_base
    return accumulated_string