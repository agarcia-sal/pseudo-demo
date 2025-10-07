from typing import List


def max_fill(grid: List[List[int]], capacity: int) -> int:
    def helper(index: int, acc: int) -> int:
        if index >= len(grid):
            return acc
        row_total = sum(grid[index])
        # ceiling division of row_total by capacity
        ceil_div = -(-row_total // capacity)
        return helper(index + 1, acc + ceil_div)

    return helper(0, 0)