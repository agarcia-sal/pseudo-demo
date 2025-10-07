from math import ceil
from typing import List

def sum_squares(list_of_numbers: List[float]) -> int:
    def recursive_accumulate(idx: int, accumulator: int) -> int:
        if idx >= len(list_of_numbers):
            return accumulator
        current_value = list_of_numbers[idx]
        updated_accumulator = accumulator + ceil(current_value) * ceil(current_value)
        return recursive_accumulate(idx + 1, updated_accumulator)

    return recursive_accumulate(0, 0)