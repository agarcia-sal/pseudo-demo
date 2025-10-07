from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    m = len(grid)
    limit = (m * m) + 1

    for x in range(m):
        for y in range(m):
            if grid[x][y] == 1:
                nearby_values = []
                if x > 0:
                    nearby_values.append(grid[x - 1][y])
                if y > 0:
                    nearby_values.append(grid[x][y - 1])
                if x < m - 1:
                    nearby_values.append(grid[x + 1][y])
                if y < m - 1:
                    nearby_values.append(grid[x][y + 1])
                if nearby_values:
                    limit = min(nearby_values)

    results: List[int] = []
    for index in range(k):
        element = 1 if (index % 2 == 0) else limit
        results.append(element)

    return results