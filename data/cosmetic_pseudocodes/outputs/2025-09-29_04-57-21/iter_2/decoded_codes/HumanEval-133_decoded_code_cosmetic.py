from typing import List
import math

def sum_squares(list_of_numbers: List[float]) -> int:
    accumulator: int = 0
    while list_of_numbers:
        current_value = math.ceil(list_of_numbers[0])
        accumulator += current_value * current_value
        list_of_numbers.pop(0)
    return accumulator