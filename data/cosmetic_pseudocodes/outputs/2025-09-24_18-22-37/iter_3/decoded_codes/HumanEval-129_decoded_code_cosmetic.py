from typing import List


def minPath(grid: List[List[int]], k: int) -> List[int]:
    size: int = len(grid)
    threshold: int = (size * size) + 1

    for x in range(size):
        for y in range(size):
            if grid[x][y] == 1:
                neighbours = []
                if x > 0:
                    neighbours.append(grid[x - 1][y])
                if y > 0:
                    neighbours.append(grid[x][y - 1])
                if x < size - 1:
                    neighbours.append(grid[x + 1][y])
                if y < size - 1:
                    neighbours.append(grid[x][y + 1])
                if neighbours:
                    threshold = min(neighbours)

    results: List[int] = []
    for index in range(k):
        results.append(1 if (index % 2) == 0 else threshold)

    return results