from typing import List
import math


def sum_squares(list_of_numbers: List[float]) -> int:
    accumulator: int = 0
    iterator: int = 0

    while iterator < len(list_of_numbers):
        current_value: float = list_of_numbers[iterator]
        powered_value: int = math.ceil(current_value) * math.ceil(current_value)
        accumulator += powered_value
        iterator += 1

    return accumulator