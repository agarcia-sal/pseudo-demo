import math
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    sum_result = 0
    outer_index = 0
    total_rows = len(grid)
    while outer_index < total_rows:
        inner_sum = 0
        inner_index = 0
        current_row = grid[outer_index]
        row_length = len(current_row)
        while inner_index < row_length:
            inner_sum += current_row[inner_index]
            inner_index += 1
        temp_ceil = math.ceil(inner_sum / capacity)
        sum_result += temp_ceil
        outer_index += 1
    result_value = sum_result
    return result_value