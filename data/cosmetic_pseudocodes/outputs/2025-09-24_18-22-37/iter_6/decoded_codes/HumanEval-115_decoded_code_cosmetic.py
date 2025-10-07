import math
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    xA1 = 0
    idxR = 0
    while idxR < len(grid):
        tmpRow = grid[idxR]
        sumRow = 0
        idxC = 0
        while idxC < len(tmpRow):
            sumRow += tmpRow[idxC]
            idxC += 1
        divVal = sumRow / capacity
        ceilVal = math.ceil(divVal)
        xA1 += ceilVal
        idxR += 1
    return xA1