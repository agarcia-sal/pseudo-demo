from typing import Literal


def modp(integer_n: int, integer_p: int) -> int:
    accumulator: int = 1
    counter: int = 0
    while counter < integer_n:
        doubled = accumulator * 2
        accumulator = doubled - integer_p * (doubled // integer_p)
        counter += 1
    return accumulator