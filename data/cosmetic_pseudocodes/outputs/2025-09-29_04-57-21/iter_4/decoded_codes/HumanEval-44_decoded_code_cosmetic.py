from typing import Literal

def change_base(integer_x: int, integer_base: int) -> str:
    converted_string: str = ""
    while integer_x > 0:
        remainder_val: int = integer_x - (integer_base * (integer_x // integer_base))
        converted_string = str(remainder_val) + converted_string
        integer_x = integer_x // integer_base
    return converted_string