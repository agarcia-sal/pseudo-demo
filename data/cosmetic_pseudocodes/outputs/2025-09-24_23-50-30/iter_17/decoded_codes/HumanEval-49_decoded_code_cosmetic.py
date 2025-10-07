from typing import Literal

def modp(integer_n: int, integer_p: int) -> int:
    accum: int = 1
    iterator: int = 0
    while iterator < integer_n:
        accum = (accum * 2) - ((accum * 2) // integer_p) * integer_p
        iterator += 1
    return accum