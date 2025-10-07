from typing import List


def minPath(grid: List[List[int]], k: int) -> List[int]:
    lengthGrid: int = len(grid)
    limitVal: int = lengthGrid * lengthGrid + 1

    for rowIndex in range(lengthGrid):
        for colIndex in range(lengthGrid):
            if grid[rowIndex][colIndex] == 1:
                neighbors: List[int] = []

                if rowIndex > 0:
                    neighbors.append(grid[rowIndex - 1][colIndex])
                if colIndex > 0:
                    neighbors.append(grid[rowIndex][colIndex - 1])
                if rowIndex < lengthGrid - 1:
                    neighbors.append(grid[rowIndex + 1][colIndex])
                if colIndex < lengthGrid - 1:
                    neighbors.append(grid[rowIndex][colIndex + 1])

                # Update limitVal to the minimum neighbor value
                if neighbors:
                    limitVal = neighbors[0]
                    idx = 1
                    while idx < len(neighbors):
                        if neighbors[idx] < limitVal:
                            limitVal = neighbors[idx]
                        idx += 1

    resultList: List[int] = []
    counter: int = 0
    while counter < k:
        if (counter % 2) != 1:
            resultList.append(1)
        else:
            resultList.append(limitVal)
        counter += 1

    return resultList