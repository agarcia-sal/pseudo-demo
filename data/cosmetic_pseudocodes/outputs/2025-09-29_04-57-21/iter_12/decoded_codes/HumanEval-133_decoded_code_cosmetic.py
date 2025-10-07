from math import ceil
from typing import List


def sum_squares(list_of_numbers: List[float]) -> int:
    accumulator: int = 0
    index: int = 0
    while index < len(list_of_numbers):
        current_value: float = list_of_numbers[index]
        elevated: int = ceil(current_value)
        elevated_squared: int = elevated * elevated
        accumulator += elevated_squared
        index += 1
    return accumulator