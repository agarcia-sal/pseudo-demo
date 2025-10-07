from math import ceil
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_fill = 0
    for row_data in grid:
        row_sum = 0
        idx = 0
        while idx < len(row_data):
            row_sum += row_data[idx]
            idx += 1
        fill_units = ceil(row_sum / capacity)
        total_fill += fill_units
    return total_fill