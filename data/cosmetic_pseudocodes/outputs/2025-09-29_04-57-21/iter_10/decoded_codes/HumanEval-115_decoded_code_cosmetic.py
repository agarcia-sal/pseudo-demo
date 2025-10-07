from typing import List
import math

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_count = 0
    index = 0
    while index < len(grid):
        current_row = grid[index]
        row_total = 0
        position = 0
        while position < len(current_row):
            row_total += current_row[position]
            position += 1
        total_count += math.ceil(row_total / capacity)
        index += 1
    return total_count