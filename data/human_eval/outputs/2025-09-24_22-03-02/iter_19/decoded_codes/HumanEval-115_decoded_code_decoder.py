import math
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_times = 0
    for index_row in range(len(grid)):
        current_row = grid[index_row]
        sum_units = 0
        for index_unit in range(len(current_row)):
            sum_units += current_row[index_unit]

        math_ceil_result = math.ceil(sum_units / capacity)
        total_times += math_ceil_result

    return total_times