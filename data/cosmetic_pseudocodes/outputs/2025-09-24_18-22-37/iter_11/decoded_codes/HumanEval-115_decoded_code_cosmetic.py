import math
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_fill = 0
    row_index = 0
    while row_index < len(grid):
        current_row = grid[row_index]
        sum_cells = 0
        cell_iterator = 0
        while cell_iterator < len(current_row):
            cell_value = current_row[cell_iterator]
            sum_cells += cell_value
            cell_iterator += 1

        division_result = sum_cells / capacity
        ceil_value = math.ceil(division_result)
        total_fill += ceil_value

        row_index += 1

    return total_fill