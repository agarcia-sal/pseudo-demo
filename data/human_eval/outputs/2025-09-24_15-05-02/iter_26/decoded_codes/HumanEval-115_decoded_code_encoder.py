from math import ceil
from typing import List

def max_fill(grid_of_lists_of_zeros_and_ones: List[List[int]], capacity: int) -> int:
    if capacity <= 0:
        raise ValueError("capacity must be a positive integer")
    return sum(ceil(sum(well_row) / capacity) for well_row in grid_of_lists_of_zeros_and_ones)