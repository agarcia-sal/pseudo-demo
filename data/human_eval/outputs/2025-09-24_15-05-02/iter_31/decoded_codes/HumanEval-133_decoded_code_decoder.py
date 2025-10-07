from math import ceil
from typing import List

def sum_squares(list_of_numbers: List[float]) -> int:
    squared_sum = 0
    for number in list_of_numbers:
        squared_sum += ceil(number) ** 2
    return squared_sum