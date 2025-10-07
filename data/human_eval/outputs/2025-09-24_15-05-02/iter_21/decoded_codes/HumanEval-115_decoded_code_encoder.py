from math import ceil
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_operations: int = 0
    for well in grid:
        water_units: int = sum(well)
        lowers_needed: int = ceil(water_units / capacity)
        total_operations += lowers_needed
    return total_operations