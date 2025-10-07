import math
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_lowerings = 0
    for well_row in grid:
        water_units = sum(well_row)
        lowerings_for_well = math.ceil(water_units / capacity)
        total_lowerings += lowerings_for_well
    return total_lowerings