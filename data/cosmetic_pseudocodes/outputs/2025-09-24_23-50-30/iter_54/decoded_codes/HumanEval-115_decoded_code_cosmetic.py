from typing import List
import math


def max_fill(grid: List[List[int]], capacity: int) -> int:
    def accumulate_rows(idx: int, acc: int) -> int:
        if idx >= len(grid):
            return acc
        return accumulate_rows(idx + 1, acc + sum(grid[idx]))

    def ceiling_division(val: int) -> int:
        return math.ceil(val / capacity)

    def sum_ceilings(idx: int, total: int) -> int:
        if idx >= len(grid):
            return total
        return sum_ceilings(idx + 1, total + ceiling_division(sum(grid[idx])))

    return sum_ceilings(0, 0)