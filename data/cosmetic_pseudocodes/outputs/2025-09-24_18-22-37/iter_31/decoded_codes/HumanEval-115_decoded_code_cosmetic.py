import math
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_fill: int = 0
    for row in grid:
        sum_elements: int = sum(row)
        ratio: float = sum_elements / capacity
        ceil_ratio: int = math.ceil(ratio)
        total_fill += ceil_ratio
    return total_fill