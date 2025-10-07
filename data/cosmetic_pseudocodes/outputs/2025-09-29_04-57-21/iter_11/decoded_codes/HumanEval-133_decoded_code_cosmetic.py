from math import ceil
from typing import Sequence

def sum_squares(sequence: Sequence[float]) -> int:
    accumulator: int = 0
    iterator: int = 0
    length = len(sequence)
    while iterator < length:
        current_value = sequence[iterator]
        elevated_value = ceil(current_value)
        powered_value = elevated_value * elevated_value
        accumulator += powered_value
        iterator += 1
    return accumulator