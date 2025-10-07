import math
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_fill = 0
    for row in grid:
        row_sum = sum(row)
        fills_needed = math.ceil(row_sum / capacity)
        total_fill += fills_needed
    return total_fill