from math import ceil
from typing import List

def sum_squares(list_of_numbers: List[float]) -> int:
    squared_sum: int = 0
    for number in list_of_numbers:
        ceiling_value: int = ceil(number)
        squared_sum += ceiling_value * ceiling_value
    return squared_sum