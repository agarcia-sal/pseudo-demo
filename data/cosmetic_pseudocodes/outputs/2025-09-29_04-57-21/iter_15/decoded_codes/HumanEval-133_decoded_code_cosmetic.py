from typing import List
import math

def sum_squares(list_of_numbers: List[float]) -> int:
    accumulator: int = 0
    index: int = 0
    while index < len(list_of_numbers):
        current_value: float = list_of_numbers[index]
        temp: int = math.ceil(current_value)
        accumulator += temp * temp
        index += 1
    return accumulator