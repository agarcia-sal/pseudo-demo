from math import ceil, pow
from typing import List

def sum_squares(list_of_numbers: List[float]) -> float:
    def helper(current_index: int, total: float) -> float:
        if current_index > len(list_of_numbers):
            return total
        value = list_of_numbers[current_index - 1]
        updated_total = total + pow(ceil(value), 2)
        return helper(current_index + 1, updated_total)
    return helper(1, 0.0)