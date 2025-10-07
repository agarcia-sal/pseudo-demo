import math
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_fills = 0
    for row_element in grid:
        row_sum = sum(row_element)
        fill_count = math.ceil(row_sum / capacity)
        total_fills += fill_count
    return total_fills