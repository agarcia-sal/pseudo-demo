from math import ceil
from typing import List

def sum_squares(list_of_numbers: List[float]) -> int:
    squared_sum: int = 0
    for number in list_of_numbers:
        rounded_number: int = ceil(number)
        squared_sum += rounded_number * rounded_number
    return squared_sum