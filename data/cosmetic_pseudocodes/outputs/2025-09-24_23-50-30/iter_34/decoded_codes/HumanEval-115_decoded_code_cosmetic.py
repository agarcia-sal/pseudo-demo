import math
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    accList: List[int] = []
    for idx in range(len(grid)):
        tempSum: int = 0
        rowData: List[int] = grid[idx]
        for elemIdx in range(len(rowData)):
            tempSum += rowData[elemIdx]
        accList.append(math.ceil(tempSum / capacity))
    totalValue: int = 0
    accIdx: int = 0
    while accIdx < len(accList):
        totalValue += accList[accIdx]
        accIdx += 1
    return totalValue