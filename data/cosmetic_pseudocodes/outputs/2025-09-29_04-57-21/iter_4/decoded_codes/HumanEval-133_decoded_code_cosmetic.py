from typing import Sequence
import math

def sum_squares(array_of_values: Sequence[float]) -> int:
    accumulator: int = 0
    iterator: int = 0
    while iterator < len(array_of_values):
        current_val: float = array_of_values[iterator]
        increment_value: int = math.ceil(current_val) * math.ceil(current_val)
        accumulator += increment_value
        iterator += 1
    return accumulator