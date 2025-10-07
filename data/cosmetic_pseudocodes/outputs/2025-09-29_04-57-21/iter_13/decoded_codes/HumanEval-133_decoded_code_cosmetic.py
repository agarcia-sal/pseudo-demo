from math import ceil
from typing import List

def sum_squares(list_of_numbers: List[float]) -> int:
    accumulator: int = 0

    def helper(index: int) -> None:
        nonlocal accumulator
        if index == len(list_of_numbers):
            return
        current_value = list_of_numbers[index]
        increment = ceil(current_value) ** 2
        accumulator += increment
        helper(index + 1)

    helper(0)
    return accumulator