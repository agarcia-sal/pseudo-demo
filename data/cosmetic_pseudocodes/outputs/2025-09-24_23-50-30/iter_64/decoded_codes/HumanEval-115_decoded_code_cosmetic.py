import math
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    sum_result: int = 0
    index: int = 0
    grid_length: int = len(grid)

    while index < grid_length:
        current_row: List[int] = grid[index]
        row_sum: int = sum(current_row)
        sum_result += math.ceil(row_sum / capacity)
        index += 1

    return sum_result