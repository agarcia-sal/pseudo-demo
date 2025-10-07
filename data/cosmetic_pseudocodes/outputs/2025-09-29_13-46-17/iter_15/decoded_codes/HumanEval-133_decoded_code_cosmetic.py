from math import ceil
from typing import List

def sum_squares(list_of_numbers: List[float]) -> int:
    def rec_accumulate(idx: int, accum: int) -> int:
        if idx >= len(list_of_numbers):
            return accum
        current = list_of_numbers[idx]

        def power_two(base: int, exp: int, result: int) -> int:
            if exp == 0:
                return result
            return power_two(base, exp - 1, result * base)

        elevated = power_two(ceil(current), 2, 1)
        return rec_accumulate(idx + 1, accum + elevated)

    return rec_accumulate(0, 0)