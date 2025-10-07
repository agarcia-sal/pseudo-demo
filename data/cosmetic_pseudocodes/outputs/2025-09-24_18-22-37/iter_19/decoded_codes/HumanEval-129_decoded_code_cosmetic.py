from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    size: int = len(grid)
    limitVal: int = size * size + 1

    rowIndex: int = 0
    while rowIndex < size:
        colIndex: int = 0
        while colIndex < size:
            if grid[rowIndex][colIndex] == 1:
                neighbours: List[int] = []

                if rowIndex != 0:
                    neighbours.append(grid[rowIndex - 1][colIndex])
                if colIndex != 0:
                    neighbours.append(grid[rowIndex][colIndex - 1])
                if rowIndex != size - 1:
                    neighbours.append(grid[rowIndex + 1][colIndex])
                if colIndex != size - 1:
                    neighbours.append(grid[rowIndex][colIndex + 1])

                minimalNeighbour = neighbours[0]
                counterIndex = 1
                while counterIndex < len(neighbours):
                    if neighbours[counterIndex] < minimalNeighbour:
                        minimalNeighbour = neighbours[counterIndex]
                    counterIndex += 1

                limitVal = minimalNeighbour
            colIndex += 1
        rowIndex += 1

    result: List[int] = []
    iterator = 0
    while iterator < k:
        if iterator % 2 == 0:
            result.append(0x1)
        else:
            result.append(limitVal)
        iterator += 1

    return result