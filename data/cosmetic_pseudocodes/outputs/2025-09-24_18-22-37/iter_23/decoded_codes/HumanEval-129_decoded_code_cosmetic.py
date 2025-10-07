from typing import List


def minPath(grid: List[List[int]], k: int) -> List[int]:
    size: int = len(grid)
    threshold: int = (size * size) + 1

    rowIndex: int = 0
    while rowIndex <= size - 1:
        colIndex: int = 0
        while colIndex <= size - 1:
            if grid[rowIndex][colIndex] == 1:
                neighbors: List[int] = []
                if rowIndex != 0:
                    aboveCell = grid[rowIndex - 1][colIndex]
                    neighbors.append(aboveCell)
                if colIndex != 0:
                    leftCell = grid[rowIndex][colIndex - 1]
                    neighbors.append(leftCell)
                if rowIndex != (size - 1):
                    belowCell = grid[rowIndex + 1][colIndex]
                    neighbors.append(belowCell)
                if colIndex != (size - 1):
                    rightCell = grid[rowIndex][colIndex + 1]
                    neighbors.append(rightCell)
                if neighbors:  # Check to avoid min on empty list, if isolated 1 cell
                    minNeighbor = neighbors[0]
                    for idx in range(1, len(neighbors)):
                        currentVal = neighbors[idx]
                        if currentVal < minNeighbor:
                            minNeighbor = currentVal
                    threshold = minNeighbor
            colIndex += 1
        rowIndex += 1

    resultArr: List[int] = []
    count: int = 0
    while count < k:
        # count % 2 == 0 → append 1, else append threshold
        if count % 2 == 0:
            resultArr.append(1)
        else:
            resultArr.append(threshold)
        count += 1

    return resultArr