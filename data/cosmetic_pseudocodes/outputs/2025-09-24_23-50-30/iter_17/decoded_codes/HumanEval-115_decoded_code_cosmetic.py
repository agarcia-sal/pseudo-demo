from typing import List
from math import floor

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_value: int = 0
    for current_row in grid:
        row_sum: int = 0
        iterator: int = 0
        while iterator < len(current_row):
            row_sum += current_row[iterator]
            iterator += 1
        row_fraction: float = row_sum / capacity
        row_ceiled: int = int(row_fraction) if row_fraction == floor(row_fraction) else int(floor(row_fraction) + 1)
        total_value += row_ceiled
    return total_value