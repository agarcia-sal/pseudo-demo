import math
from typing import List

def max_fill(grid: List[List[float]], capacity: float) -> int:
    result_sum: int = 0
    for current_row in grid:
        row_accumulator: float = sum(current_row)
        division_result: float = row_accumulator / capacity
        partial_ceil: int = math.ceil(division_result)
        result_sum += partial_ceil
    return result_sum