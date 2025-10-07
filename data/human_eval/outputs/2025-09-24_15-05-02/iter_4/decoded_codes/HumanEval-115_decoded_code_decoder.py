import math
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_lowerings = 0
    for well in grid:
        water_units = sum(well)
        lowers_needed = math.ceil(water_units / capacity)
        total_lowerings += lowers_needed
    return total_lowerings