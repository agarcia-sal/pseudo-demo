import math
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_times = 0
    for well in grid:
        water_units = sum(well)
        times_for_well = math.ceil(water_units / capacity)
        total_times += times_for_well
    return total_times