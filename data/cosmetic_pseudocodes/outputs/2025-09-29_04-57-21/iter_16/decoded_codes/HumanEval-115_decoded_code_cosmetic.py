from typing import List
import math

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_fill = 0
    for row_element in grid:
        row_sum = 0
        for cell_value in row_element:
            row_sum += cell_value
        total_fill += math.ceil(row_sum / capacity)
    return total_fill