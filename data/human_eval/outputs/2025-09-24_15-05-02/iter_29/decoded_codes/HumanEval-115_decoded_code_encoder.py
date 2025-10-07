from math import ceil
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_bucket_lowerings = 0
    for well_row in grid:
        water_units_in_well = sum(well_row)
        lowers_for_well = ceil(water_units_in_well / capacity) if capacity > 0 else 0
        total_bucket_lowerings += lowers_for_well
    return total_bucket_lowerings