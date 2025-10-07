import math
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_sum = 0
    idx = 0
    while idx < len(grid):
        current_line = grid[idx]
        line_total = 0
        for element in current_line:
            line_total += element
        increment = math.ceil(line_total / capacity)
        total_sum += increment
        idx += 1
    return total_sum