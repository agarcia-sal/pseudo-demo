import math
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_sum = 0
    for row_element in grid:
        row_accumulator = 0
        index = 0
        while index < len(row_element):
            row_accumulator += row_element[index]
            index += 1
        ceil_value = math.ceil(row_accumulator / capacity)
        total_sum += ceil_value
    return total_sum