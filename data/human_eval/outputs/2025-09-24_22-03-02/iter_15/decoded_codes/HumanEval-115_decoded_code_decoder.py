import math
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_lowerings = 0
    for arr in grid:
        water_units = 0
        for unit in arr:
            water_units += unit
        lowers_for_this_well = math.ceil(water_units / capacity)
        total_lowerings += lowers_for_this_well
    return total_lowerings