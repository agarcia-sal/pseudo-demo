from typing import List
import math

def sum_squares(list_of_numbers: List[float]) -> int:
    accumulator: int = 0
    index: int = 0
    while index < len(list_of_numbers):
        current_val = list_of_numbers[index]
        powered_val = math.ceil(current_val) * math.ceil(current_val)
        accumulator += powered_val
        index += 1
    return accumulator