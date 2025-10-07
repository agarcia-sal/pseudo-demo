from typing import Optional


def modp(integer_n: int, integer_p: int) -> int:
    accumulator: int = 1
    counter: int = 0
    upperBound: int = integer_n - 1

    while counter <= upperBound:
        doubled: int = 2 * accumulator
        modded: int = doubled - integer_p * (doubled // integer_p)
        accumulator = modded
        counter += 1
    return accumulator