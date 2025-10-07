from typing import List


def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_sum = 0
    for row in grid:
        row_sum = sum(row)
        total_sum += (row_sum + capacity - 1) // capacity  # ceiling division for row_sum / capacity
    return total_sum