from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    size: int = len(grid)
    boundary: int = (size * size) + 1

    for rowIndex in range(size):
        for colIndex in range(size):
            cellValue: int = grid[rowIndex][colIndex]
            if cellValue == 1:
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
                    minimumNeighbor: int = neighbors[0]
                    for idx in range(1, len(neighbors)):
                        if neighbors[idx] < minimumNeighbor:
                            minimumNeighbor = neighbors[idx]
                    boundary = minimumNeighbor

    resultSequence: List[int] = []

    def fillAnswer(index: int) -> None:
        if index >= k:
            return
        if index % 2 == 0:
            resultSequence.append(1)
        else:
            resultSequence.append(boundary)
        fillAnswer(index + 1)

    fillAnswer(0)
    return resultSequence