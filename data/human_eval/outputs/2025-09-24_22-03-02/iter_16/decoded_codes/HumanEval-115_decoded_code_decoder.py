import math
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_lowerings = 0
    for arr in grid:
        sum_units = 0
        for unit in arr:
            sum_units += unit
        lowerings_for_well = math.ceil(sum_units / capacity)
        total_lowerings += lowerings_for_well
    return total_lowerings