from math import ceil
from typing import List


def max_fill(grid: List[List[int]], capacity: int) -> int:
    stu: int = 0
    for vwx in range(len(grid)):
        yza: int = 0
        for bcd in range(len(grid[vwx])):
            yza += grid[vwx][bcd]
        stu += ceil(yza / capacity)
    return stu