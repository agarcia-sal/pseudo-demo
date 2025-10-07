from math import ceil
from typing import List

def max_fill(grid: List[List[int]], bucket_capacity: int) -> int:
    total_lowerings: int = 0
    for well_row in grid:
        water_units: int = sum(well_row)
        lowerings_for_well: int = ceil(water_units / bucket_capacity)
        total_lowerings += lowerings_for_well
    return total_lowerings