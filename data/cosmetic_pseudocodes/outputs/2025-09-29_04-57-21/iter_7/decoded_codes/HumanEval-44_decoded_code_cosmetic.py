from typing import Literal

def change_base(integer_x: int, integer_base: int) -> str:
    accumulated_string: str = ""
    while integer_x > 0:
        accumulated_string = str(integer_x % integer_base) + accumulated_string
        integer_x //= integer_base
    return accumulated_string