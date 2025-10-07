from typing import Literal

def modp(integer_n: int, integer_p: int) -> int:
    temp_counter = 0
    accumulator = 1
    while temp_counter < integer_n:
        intermediate = accumulator * 2
        accumulator = intermediate - ((intermediate // integer_p) * integer_p)
        temp_counter += 1
    return accumulator