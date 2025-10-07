from typing import List


def max_fill(grid: List[List[int]], capacity: int) -> int:
    total: int = 0
    for row in grid:
        row_sum: int = sum(row)
        value: float = row_sum / capacity
        ceil_value: int = int(value) if value == int(value) else int(value) + 1
        total += ceil_value
    return total