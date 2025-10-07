from math import ceil
from typing import List


def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_fill = 0
    for each_row in grid:
        row_total = sum(each_row)
        partial = ceil(row_total / capacity)
        total_fill += partial
    return total_fill