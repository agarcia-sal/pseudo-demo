from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    p: int = len(grid)
    q: int = p * p + 1

    def processIndices(x: int, y: int) -> None:
        nonlocal q
        if grid[x][y] == 1:
            tempVals: List[int] = []
            if x != 0:
                tempVals.append(grid[x - 1][y])
            if y != 0:
                tempVals.append(grid[x][y - 1])
            if x != p - 1:
                tempVals.append(grid[x + 1][y])
            if y != p - 1:
                tempVals.append(grid[x][y + 1])
            if tempVals:
                q = min(q, min(tempVals))
        if y + 1 < p:
            processIndices(x, y + 1)
        elif x + 1 < p:
            processIndices(x + 1, 0)

    processIndices(0, 0)

    result: List[int] = []
    for r in range(k):
        if r % 2 == 0:
            result.append(1)
        else:
            result.append(q)

    return result