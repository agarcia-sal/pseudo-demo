import math
from typing import List


def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_fillings: int = 0
    row_idx: int = 0
    while row_idx < len(grid):
        current_row: List[int] = grid[row_idx]
        sum_row: int = 0
        elem_idx: int = 0
        while elem_idx < len(current_row):
            sum_row += current_row[elem_idx]
            elem_idx += 1
        fraction: float = sum_row / capacity
        rounded_up: int = math.ceil(fraction)
        total_fillings += rounded_up
        row_idx += 1
    return total_fillings