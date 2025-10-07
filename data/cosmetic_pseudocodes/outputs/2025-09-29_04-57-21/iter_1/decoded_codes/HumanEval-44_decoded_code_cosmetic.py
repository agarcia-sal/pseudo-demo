from typing import Literal

def change_base(integer_x: int, integer_base: int) -> str:
    string_result: str = ""
    while integer_x > 0:
        remainder: int = integer_x % integer_base
        string_result = str(remainder) + string_result
        integer_x = integer_x // integer_base  # use integer division to floor
    return string_result