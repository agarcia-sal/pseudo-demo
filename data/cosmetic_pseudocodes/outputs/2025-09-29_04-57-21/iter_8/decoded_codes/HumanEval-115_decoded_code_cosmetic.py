from typing import List
import math

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_sum: int = 0
    queue_rows: List[List[int]] = grid.copy()
    while queue_rows:
        next_row = queue_rows.pop(0)
        row_accum = 0
        idx = 0
        while idx < len(next_row):
            row_accum += next_row[idx]
            idx += 1
        total_sum += math.ceil(row_accum / capacity)
    return total_sum