from math import ceil
from typing import Sequence

def max_fill(grid: Sequence[Sequence[int]], capacity: int) -> int:
    total_lowerings = 0
    for single_well in grid:
        units_of_water = sum(single_well)
        times_to_lower_bucket = ceil(units_of_water / capacity)
        total_lowerings += times_to_lower_bucket
    return total_lowerings