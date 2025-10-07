from typing import List
import math

def max_fill(grid: List[List[int]], capacity: int) -> int:
    if capacity <= 0:
        raise ValueError("capacity must be a positive integer")
    total_lowerings: int = 0
    for well_row in grid:
        water_units: int = sum(well_row)
        lowerings_for_well: int = math.ceil(water_units / capacity)
        total_lowerings += lowerings_for_well
    return total_lowerings