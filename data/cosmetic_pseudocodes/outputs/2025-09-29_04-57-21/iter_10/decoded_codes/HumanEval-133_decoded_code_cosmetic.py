from math import ceil
from typing import List


def sum_squares(list_of_numbers: List[float]) -> int:
    total: int = 0
    idx: int = 0
    while idx < len(list_of_numbers):
        current_value: float = list_of_numbers[idx]
        ceil_value: int = ceil(current_value)
        squared: int = ceil_value * ceil_value
        total += squared
        idx += 1
    return total