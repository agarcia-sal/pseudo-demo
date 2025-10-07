from math import ceil
from typing import List

def sum_squares(list_of_numbers: List[float]) -> int:
    def helper(index: int, accum: int) -> int:
        if index == len(list_of_numbers):
            return accum
        current_val = list_of_numbers[index]
        updated_accum = accum + (ceil(current_val) * ceil(current_val))
        return helper(index + 1, updated_accum)
    return helper(0, 0)