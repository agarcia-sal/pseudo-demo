from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    size: int = len(grid)
    limit: int = size * size + 1

    for x in range(size):
        for y in range(size):
            if grid[x][y] == 1:
                neighbors: List[int] = []
                if x > 0:
                    neighbors.append(grid[x - 1][y])
                if y > 0:
                    neighbors.append(grid[x][y - 1])
                if x < size - 1:
                    neighbors.append(grid[x + 1][y])
                if y < size - 1:
                    neighbors.append(grid[x][y + 1])
                if neighbors:  # Only update limit if neighbors is not empty
                    limit = min(limit, *neighbors)

    result: List[int] = []
    for z in range(k):
        result.append(limit if z % 2 == 1 else 1)

    return result