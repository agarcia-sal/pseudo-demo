from math import ceil
from typing import List


def max_fill(grid: List[List[int]], capacity: int) -> int:
    def processRows(idx: int, accumulated: int) -> int:
        if idx >= len(grid):
            return accumulated
        sumCurrentRow = sum(grid[idx])
        currentFill = ceil(sumCurrentRow / capacity)
        return processRows(idx + 1, accumulated + currentFill)

    return processRows(0, 0)