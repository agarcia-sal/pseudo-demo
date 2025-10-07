from math import ceil
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_fill = 0
    for row in grid:
        row_sum = sum(row)
        total_fill += ceil(row_sum / capacity)
    return total_fill