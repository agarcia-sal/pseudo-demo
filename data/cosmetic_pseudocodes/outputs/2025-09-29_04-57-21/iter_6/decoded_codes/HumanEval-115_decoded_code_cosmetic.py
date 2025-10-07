from typing import List
import math

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total = 0
    for row in grid:
        subtotal = sum(row)
        total += math.ceil(subtotal / capacity)
    return total