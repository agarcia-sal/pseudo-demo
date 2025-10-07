from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    n: int = len(grid)
    range_limit: int = n * n + 1

    for x in range(n):
        for y in range(n):
            if grid[x][y] == 1:
                neighbors = set()
                if x > 0:
                    neighbors.add(grid[x - 1][y])
                if y > 0:
                    neighbors.add(grid[x][y - 1])
                if x < n - 1:
                    neighbors.add(grid[x + 1][y])
                if y < n - 1:
                    neighbors.add(grid[x][y + 1])
                if neighbors:
                    range_limit = min(range_limit, min(neighbors))

    result: List[int] = []
    for z in range(k):
        if z % 2 == 0:
            result.append(1)
        else:
            result.append(range_limit)

    return result