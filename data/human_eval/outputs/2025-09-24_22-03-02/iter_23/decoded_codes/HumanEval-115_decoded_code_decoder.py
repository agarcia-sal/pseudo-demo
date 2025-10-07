import math
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_times = 0
    outer_index = 0
    while outer_index < len(grid):
        current_row = grid[outer_index]
        sum_units = 0
        inner_index = 0
        while inner_index < len(current_row):
            sum_units += current_row[inner_index]
            inner_index += 1
        times_for_row = math.ceil(sum_units / capacity)
        total_times += times_for_row
        outer_index += 1
    return total_times