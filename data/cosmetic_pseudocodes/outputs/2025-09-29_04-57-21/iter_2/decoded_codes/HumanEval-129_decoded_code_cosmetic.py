from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    size: int = len(grid)
    threshold: int = size * size + 1

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
                    threshold = min(threshold, min(neighbors))

    results: List[int] = []
    index: int = 0
    while index < k:
        if index % 2 == 0:
            results.append(1)
        else:
            results.append(threshold)
        index += 1

    return results