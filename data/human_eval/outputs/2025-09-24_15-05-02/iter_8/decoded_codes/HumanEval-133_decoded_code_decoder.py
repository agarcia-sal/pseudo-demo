from typing import List
from math import ceil

def sum_squares(list_of_numbers: List[float]) -> int:
    squared_sum: int = 0
    for number in list_of_numbers:
        squared_sum += ceil(number) ** 2
    return squared_sum