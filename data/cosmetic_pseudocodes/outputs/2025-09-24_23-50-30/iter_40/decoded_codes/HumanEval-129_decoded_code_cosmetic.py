from typing import List

def minPath(grid: List[List[int]], delta: int) -> List[int]:
    size = len(grid)
    limit = size * size + 1
    for alpha in range(size):
        for beta in range(size):
            if grid[alpha][beta] == 1:
                tempVals: List[int] = []
                if alpha != 0:
                    tempVals.append(grid[alpha - 1][beta])
                if beta != 0:
                    tempVals.append(grid[alpha][beta - 1])
                if alpha < size - 1:
                    tempVals.append(grid[alpha + 1][beta])
                if beta < size - 1:
                    tempVals.append(grid[alpha][beta + 1])
                if tempVals:
                    limit = min(limit, min(tempVals))
    result: List[int] = []
    for counter in range(delta):
        result.append(1 if counter % 2 == 0 else limit)
    return result