import math
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_fill = 0
    for row_item in grid:
        accumulated = 0
        index = 0
        while index < len(row_item):
            accumulated += row_item[index]
            index += 1
        division_result = accumulated / capacity
        rounded_value = math.ceil(division_result)
        total_fill += rounded_value
    return total_fill