from math import ceil
from typing import List

def sum_squares(list_of_numbers: List[float]) -> int:
    def helper(accum: int, idx: int) -> int:
        if idx >= len(list_of_numbers):
            return accum
        current = list_of_numbers[idx]
        temp_val = ceil(current)
        powered = temp_val * temp_val
        new_accum = accum + powered
        return helper(new_accum, idx + 1)
    return helper(0, 0)