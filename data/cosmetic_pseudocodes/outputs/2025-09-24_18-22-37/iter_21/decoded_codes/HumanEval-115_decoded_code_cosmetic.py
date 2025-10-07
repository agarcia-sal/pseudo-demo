import math
from typing import List

def max_fill(grid: List[List[float]], capacity: float) -> int:
    row_sum_list: List[float] = []
    idx: int = 0
    while True:
        if idx >= len(grid):
            break
        temp_sum: float = 0
        elem_idx: int = 0
        while True:
            if elem_idx >= len(grid[idx]):
                break
            temp_sum += grid[idx][elem_idx]
            elem_idx += 1
        row_sum_list.append(temp_sum)
        idx += 1
    total_ceiled: int = 0
    row_iter: int = 0
    while row_iter < len(row_sum_list):
        division_result: float = row_sum_list[row_iter] / capacity
        ceiling_value: int = math.ceil(division_result)
        total_ceiled += ceiling_value
        row_iter += 1
    return total_ceiled