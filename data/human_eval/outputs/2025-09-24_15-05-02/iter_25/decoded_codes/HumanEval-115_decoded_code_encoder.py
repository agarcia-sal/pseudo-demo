from math import ceil
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_times = 0
    for row in grid:
        # Sum elements from index 0 up to but not including the last element in the row
        units_of_water = sum(row[:-1])
        times_for_row = ceil(units_of_water / capacity) if capacity != 0 else 0
        total_times += times_for_row
    return total_times