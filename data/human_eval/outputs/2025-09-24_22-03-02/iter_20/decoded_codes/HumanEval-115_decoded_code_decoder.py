import math
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_raises = 0
    for current_row in grid:
        sum_units = sum(current_row)
        raises_for_row = math.ceil(sum_units / capacity)
        total_raises += raises_for_row
    return total_raises