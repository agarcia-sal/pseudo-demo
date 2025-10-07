from math import ceil
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    if capacity <= 0:
        raise ValueError("capacity must be positive")
    return sum(ceil(sum(row) / capacity) for row in grid)