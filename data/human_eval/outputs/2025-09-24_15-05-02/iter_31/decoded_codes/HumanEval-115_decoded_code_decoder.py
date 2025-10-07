from math import ceil
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_lowerings = 0
    for well_row in grid:
        water_units = sum(well_row)
        lowerings_for_current_well = ceil(water_units / capacity) if capacity > 0 else 0
        total_lowerings += lowerings_for_current_well
    return total_lowerings