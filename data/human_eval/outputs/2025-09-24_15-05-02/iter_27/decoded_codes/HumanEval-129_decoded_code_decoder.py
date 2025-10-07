from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    if not grid or not grid[0]:
        raise ValueError("Grid must be a non-empty 2D list")
    n: int = len(grid)
    if any(len(row) != n for row in grid):
        raise ValueError("Grid must be a square matrix")
    if k < 0:
        raise ValueError("k must be non-negative")

    val: int = n * n + 1

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                neighbors: List[int] = []
                if i > 0:
                    neighbors.append(grid[i - 1][j])
                if j > 0:
                    neighbors.append(grid[i][j - 1])
                if i < n - 1:
                    neighbors.append(grid[i + 1][j])
                if j < n - 1:
                    neighbors.append(grid[i][j + 1])
                if neighbors:
                    val = min(val, min(neighbors))

    return [1 if idx % 2 == 0 else val for idx in range(k)]