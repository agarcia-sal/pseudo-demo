import math
from typing import List


def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_bucket_uses = 0
    for well_row in grid:
        units_of_water = sum(well_row)
        bucket_uses_for_well = math.ceil(units_of_water / capacity)
        total_bucket_uses += bucket_uses_for_well
    return total_bucket_uses