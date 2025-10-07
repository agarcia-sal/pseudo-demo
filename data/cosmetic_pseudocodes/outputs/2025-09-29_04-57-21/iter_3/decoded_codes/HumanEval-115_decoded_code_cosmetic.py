from math import ceil
from typing import List


def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_capacity_needed = 0
    for row in grid:
        row_sum = sum(row)
        fills_for_row = ceil(row_sum / capacity) if capacity != 0 else 0
        total_capacity_needed += fills_for_row
    return total_capacity_needed