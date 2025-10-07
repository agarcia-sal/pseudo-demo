import math
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    all_row_sums: List[int] = []
    iterator_index: int = 0
    max_fill_result: int = 0

    while iterator_index < len(grid):
        row_current = grid[iterator_index]
        acc_row = 0
        idx_col = 0

        while idx_col < len(row_current):
            acc_row += row_current[idx_col]
            idx_col += 1

        all_row_sums.append(acc_row)
        iterator_index += 1

    index_sum = 0
    while index_sum < len(all_row_sums):
        current_sum = all_row_sums[index_sum]
        division_result = current_sum / capacity
        ceil_value = math.ceil(division_result)
        max_fill_result += ceil_value
        index_sum += 1

    return max_fill_result