from typing import List
from math import ceil

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_lowerings: int = 0
    for well_row in grid:
        water_units: int = sum(well_row)
        # To prevent division by zero and handle edge cases, capacity must be positive
        if capacity <= 0:
            raise ValueError("capacity must be a positive integer")
        lowerings_for_well: int = ceil(water_units / capacity)
        total_lowerings += lowerings_for_well
    return total_lowerings