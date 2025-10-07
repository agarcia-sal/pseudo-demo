import math
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_lowerings = 0
    for well_row in grid:
        total_water_units = sum(well_row)
        lowers_needed = math.ceil(total_water_units / capacity)
        total_lowerings += lowers_needed
    return total_lowerings