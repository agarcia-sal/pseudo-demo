from math import ceil
from typing import Iterable

def sum_squares(list_of_numbers: Iterable[float]) -> int:
    squared_sum = 0
    for number in list_of_numbers:
        rounded_number = ceil(number)
        squared_sum += rounded_number ** 2
    return squared_sum