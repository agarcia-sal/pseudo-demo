from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    size: int = len(grid)
    minimalValue: int = size * size + 1

    rowIndex: int = 0
    while rowIndex < size:
        colIndex: int = 0
        while colIndex < size:
            if grid[rowIndex][colIndex] == 1:
                neighbors: List[int] = []
                if rowIndex > 0:
                    neighbors.append(grid[rowIndex - 1][colIndex])
                if colIndex > 0:
                    neighbors.append(grid[rowIndex][colIndex - 1])
                if rowIndex < size - 1:
                    neighbors.append(grid[rowIndex + 1][colIndex])
                if colIndex < size - 1:
                    neighbors.append(grid[rowIndex][colIndex + 1])
                if neighbors:
                    minimalValue = min(neighbors)
            colIndex += 1
        rowIndex += 1

    resultList: List[int] = []
    counter: int = 0
    while counter < k:
        if counter % 2 == 0:
            resultList.append(1)
        else:
            resultList.append(minimalValue)
        counter += 1

    return resultList