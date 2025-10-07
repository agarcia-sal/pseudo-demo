from math import ceil
from typing import List


def max_fill(grid: List[List[int]], capacity: int) -> int:
    acc = 0
    for row in grid:
        row_total = sum(row)
        acc += ceil(row_total / capacity) if capacity else 0  # handle zero capacity gracefully
    return acc