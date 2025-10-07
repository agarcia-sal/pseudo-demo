from typing import List
import math

def sum_squares(list_of_numbers: List[float]) -> int:
    total: int = 0
    iterator: int = 0
    while iterator < len(list_of_numbers):
        current_value: float = list_of_numbers[iterator]
        ceil_val: int = math.ceil(current_value)
        squared_val: int = ceil_val * ceil_val
        total += squared_val
        iterator += 1
    return total