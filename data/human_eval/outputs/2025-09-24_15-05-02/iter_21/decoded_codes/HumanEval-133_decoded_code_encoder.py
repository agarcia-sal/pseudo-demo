from math import ceil
from typing import List

def sum_squares(list_of_numbers: List[float]) -> int:
    squared: int = 0
    for number in list_of_numbers:
        ceiling_number: int = ceil(number)
        squared += ceiling_number * ceiling_number
    return squared