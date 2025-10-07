import math
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total = 0
    idx = 0
    n = len(grid)
    while idx < n:
        row_sum = sum(grid[idx])
        total += math.ceil(row_sum / capacity)
        idx += 1
    return total