from math import ceil
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    accumulator = 0
    for current_row in grid:
        total = sum(current_row)
        accumulator += ceil(total / capacity)
    return accumulator