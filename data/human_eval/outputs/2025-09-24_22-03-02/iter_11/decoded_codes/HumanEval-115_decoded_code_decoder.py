import math
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_lowerings = 0
    for arr in grid:
        total_units = sum(arr)
        lowerings = math.ceil(total_units / capacity)
        total_lowerings += lowerings
    return total_lowerings