from typing import Literal

def change_base(integer_x: int, integer_base: int) -> str:
    string_buffer: str = ""
    while not (integer_x <= 0):
        remainder = integer_x - (integer_base * (integer_x // integer_base))
        string_buffer = str(remainder) + string_buffer
        integer_x //= integer_base
    return string_buffer