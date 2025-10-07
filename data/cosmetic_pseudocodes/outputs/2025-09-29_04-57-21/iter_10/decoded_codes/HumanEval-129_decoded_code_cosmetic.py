from typing import List


def minPath(grid: List[List[int]], k: int) -> List[int]:
    size: int = len(grid)
    threshold: int = size * size + 1

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
                    threshold = neighbors[0]
                    nIdx: int = 1
                    while nIdx < len(neighbors):
                        if neighbors[nIdx] < threshold:
                            threshold = neighbors[nIdx]
                        nIdx += 1

    resultArray: List[int] = []
    counter: int = 0
    while counter < k:
        if counter % 2 != 0:
            resultArray.append(threshold)
        else:
            resultArray.append(1)
        counter += 1

    return resultArray