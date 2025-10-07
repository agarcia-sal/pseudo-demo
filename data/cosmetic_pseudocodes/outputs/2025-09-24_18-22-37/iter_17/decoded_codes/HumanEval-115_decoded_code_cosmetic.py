import math
from typing import List


def max_fill(grid: List[List[int]], capacity: int) -> int:
    container_total = 0
    row_index = 0
    while row_index < len(grid):
        row = grid[row_index]
        row_sum = 0
        i = 0
        while i < len(row):
            row_sum += row[i]
            i += 1
        divided = row_sum / capacity
        ceiling_val = math.ceil(divided)
        container_total += ceiling_val
        row_index += 1
    return container_total