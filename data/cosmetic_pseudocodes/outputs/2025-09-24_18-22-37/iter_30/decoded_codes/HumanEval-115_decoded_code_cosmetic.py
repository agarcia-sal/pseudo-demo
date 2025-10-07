import math
from typing import List


def max_fill(grid: List[List[int]], d: int) -> int:
    total_fill: int = 0
    j: int = 0
    while j < len(grid):
        current_row: List[int] = grid[j]
        row_sum: int = 0
        k: int = 0
        while k < len(current_row):
            row_sum += current_row[k]
            k += 1
        divided_val: float = row_sum / d
        ceil_val: int = math.ceil(divided_val)
        total_fill += ceil_val
        j += 1
    return total_fill