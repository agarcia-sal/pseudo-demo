from math import ceil
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_lowerings: int = 0
    for well_row in grid:
        water_units: int = sum(well_row)
        lowers_for_well: int = ceil(water_units / capacity)
        total_lowerings += lowers_for_well
    return total_lowerings