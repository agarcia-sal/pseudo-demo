from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    size: int = len(grid)
    limit: int = (size * size) + 1

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
                    limit = min(limit, min(neighbors))

    results: List[int] = []
    for counter in range(k):
        results.append(1 if counter % 2 == 0 else limit)

    return results