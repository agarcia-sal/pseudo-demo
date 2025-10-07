from math import ceil
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    return sum(ceil(sum(arr) / capacity) for arr in grid)