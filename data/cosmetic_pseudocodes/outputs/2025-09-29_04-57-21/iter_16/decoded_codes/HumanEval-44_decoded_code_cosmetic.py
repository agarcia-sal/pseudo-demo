from typing import Literal

def change_base(integer_x: int, integer_base: int) -> str:
    accumulator: str = ""
    while integer_x != 0:
        digit_char = str(integer_x % integer_base)
        accumulator = digit_char + accumulator
        integer_x //= integer_base
    return accumulator