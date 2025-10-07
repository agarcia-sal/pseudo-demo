from math import ceil
from typing import List

def sum_squares(list_of_numbers: List[float]) -> int:
    squared_sum: int = 0
    for element in list_of_numbers:
        rounded_element: int = ceil(element)
        squared_sum += rounded_element ** 2
    return squared_sum