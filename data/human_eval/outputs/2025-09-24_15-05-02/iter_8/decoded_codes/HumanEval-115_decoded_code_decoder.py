from math import ceil
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_lowerings: int = 0
    for well in grid:
        water_units = sum(well)
        lowerings_for_well = ceil(water_units / capacity) if capacity > 0 else 0
        total_lowerings += lowerings_for_well
    return total_lowerings