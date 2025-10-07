import math
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total = 0
    for row_element in grid:
        row_sum = sum(row_element)
        increments = row_sum / capacity
        rounded = math.ceil(increments)
        total += rounded
    return total