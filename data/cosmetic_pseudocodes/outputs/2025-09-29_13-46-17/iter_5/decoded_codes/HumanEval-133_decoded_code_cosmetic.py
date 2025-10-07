from typing import List
import math


def sum_squares(list_of_numbers: List[float]) -> int:
    def helper(accumulator: int, index: int) -> int:
        if index >= len(list_of_numbers):
            return accumulator
        current_val_snake = list_of_numbers[index]
        next_accumulator = accumulator + (math.ceil(current_val_snake) ** 2)
        return helper(next_accumulator, index + 1)

    return helper(0, 0)