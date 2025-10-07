from math import ceil
from typing import List

def sum_squares(list_of_numbers: List[float]) -> int:
    sum_of_squares: int = 0
    for element in list_of_numbers:
        sum_of_squares += ceil(element) ** 2
    return sum_of_squares