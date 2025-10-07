from math import ceil
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_uses = 0
    for well_row in grid:
        units_of_water = sum(well_row)
        uses_for_well = ceil(units_of_water / capacity)
        total_uses += uses_for_well
    return total_uses