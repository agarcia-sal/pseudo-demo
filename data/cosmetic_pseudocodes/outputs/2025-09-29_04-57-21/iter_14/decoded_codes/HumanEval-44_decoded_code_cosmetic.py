from typing import Literal

def change_base(integer_x: int, integer_base: int) -> str:
    accumulation: str = ""
    while not (integer_x <= 0):
        digit_string: str = str(integer_x % integer_base)
        accumulation = digit_string + accumulation
        integer_x //= integer_base
    return accumulation