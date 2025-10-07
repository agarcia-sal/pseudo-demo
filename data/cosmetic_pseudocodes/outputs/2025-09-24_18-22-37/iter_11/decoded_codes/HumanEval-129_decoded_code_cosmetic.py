from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    lengthGrid: int = len(grid)
    maxValue: int = (lengthGrid * lengthGrid) + 1

    rowIndex: int = 0
    while rowIndex < lengthGrid:
        colIndex: int = 0
        while colIndex < lengthGrid:
            if grid[rowIndex][colIndex] == 1:
                neighbors: List[int] = []
                if rowIndex != 0:
                    neighbors.append(grid[rowIndex - 1][colIndex])
                if colIndex != 0:
                    neighbors.append(grid[rowIndex][colIndex - 1])
                if rowIndex != lengthGrid - 1:
                    neighbors.append(grid[rowIndex + 1][colIndex])
                if colIndex != lengthGrid - 1:
                    neighbors.append(grid[rowIndex][colIndex + 1])

                minNeighbor: int = neighbors[0]
                nIndex: int = 1
                while nIndex < len(neighbors):
                    if minNeighbor > neighbors[nIndex]:
                        minNeighbor = neighbors[nIndex]
                    nIndex += 1

                maxValue = minNeighbor
            colIndex += 1
        rowIndex += 1

    resultList: List[int] = []
    counter: int = 0
    while counter < k:
        if counter % 2 == 0:
            resultList.append(1)
        else:
            resultList.append(maxValue)
        counter += 1

    return resultList