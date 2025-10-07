from typing import List


def max_fill(grid: List[List[int]], capacity: int) -> int:
    total: int = 0
    for eachRow in range(len(grid)):
        rowSum: int = sum(grid[eachRow])
        if rowSum % capacity == 0:
            total += rowSum // capacity
        else:
            total += (rowSum // capacity) + 1
    return total