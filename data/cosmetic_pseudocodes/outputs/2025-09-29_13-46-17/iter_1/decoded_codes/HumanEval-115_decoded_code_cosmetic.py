from math import ceil
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total = 0
    for row in grid:
        row_sum = sum(row)
        total += ceil(row_sum / capacity)
    return total