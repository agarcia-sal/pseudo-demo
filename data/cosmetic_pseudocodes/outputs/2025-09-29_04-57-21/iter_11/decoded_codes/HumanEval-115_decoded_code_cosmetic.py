import math
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total: int = 0
    row_index: int = 0
    while row_index < len(grid):
        current_row: List[int] = grid[row_index]
        row_sum: int = 0
        element_index: int = 0
        while element_index < len(current_row):
            row_sum += current_row[element_index]
            element_index += 1
        total += math.ceil(row_sum / capacity)
        row_index += 1
    return total