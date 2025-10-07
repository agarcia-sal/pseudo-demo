import math
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    accumulator: int = 0
    i: int = 0
    while i < len(grid):
        current_row: List[int] = grid[i]
        total_in_row: int = sum(current_row)
        factor: float = total_in_row / capacity
        ceiling_value: int = math.ceil(factor)
        accumulator += ceiling_value
        i += 1
    return accumulator