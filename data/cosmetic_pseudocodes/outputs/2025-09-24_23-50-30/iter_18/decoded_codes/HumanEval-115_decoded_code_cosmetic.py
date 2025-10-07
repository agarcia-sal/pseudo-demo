from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_fill: int = 0
    idx: int = 0
    while idx < len(grid):
        row_sum: int = 0
        col_idx: int = 0
        while col_idx < len(grid[idx]):
            row_sum += grid[idx][col_idx]
            col_idx += 1
        div_res: int = row_sum // capacity
        if div_res * capacity < row_sum:
            div_res += 1
        total_fill += div_res
        idx += 1
    return total_fill