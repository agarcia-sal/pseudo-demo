import math
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_fill = 0
    index = 0
    while index < len(grid):
        row_sum = 0
        for element in grid[index]:
            row_sum += element
        fill_value = math.ceil(row_sum / capacity)
        total_fill += fill_value
        index += 1
    return total_fill