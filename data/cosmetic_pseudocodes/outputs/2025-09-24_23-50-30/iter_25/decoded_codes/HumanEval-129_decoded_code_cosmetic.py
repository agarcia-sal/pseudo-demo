from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    size: int = len(grid)
    minVal: int = (size * size) + 1

    for idxX in range(size):
        for idxY in range(size):
            if grid[idxX][idxY] == 1:
                neighbors: List[int] = []

                if idxX != 0:
                    neighbors.append(grid[idxX - 1][idxY])
                if idxY != 0:
                    neighbors.append(grid[idxX][idxY - 1])
                if idxX != (size - 1):
                    neighbors.append(grid[idxX + 1][idxY])
                if idxY != (size - 1):
                    neighbors.append(grid[idxX][idxY + 1])

                if neighbors:  # Ensure neighbors is not empty before min
                    minVal = min(minVal, min(neighbors))

    resultSeq: List[int] = []
    for index in range(k):
        resultSeq.append(1 if index % 2 == 0 else minVal)

    return resultSeq