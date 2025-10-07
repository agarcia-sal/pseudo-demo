from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    size: int = len(grid)
    threshold: int = (size * size) + 1

    for rowIndex in range(size):
        for colIndex in range(size):
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
                    minimumNeighbor = neighbors[0]
                    idx = 1
                    while idx < len(neighbors):
                        if neighbors[idx] < minimumNeighbor:
                            minimumNeighbor = neighbors[idx]
                        idx += 1
                    threshold = minimumNeighbor

    result: List[int] = []
    counter: int = 0
    while counter < k:
        if (counter - 2 * (counter // 2)) == 0:  # equivalent to counter % 2 == 0
            result.append(1)
        else:
            result.append(threshold)
        counter += 1

    return result