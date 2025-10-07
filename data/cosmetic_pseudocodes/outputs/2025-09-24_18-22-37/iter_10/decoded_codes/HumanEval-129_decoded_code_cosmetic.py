from typing import List


def minPath(grid: List[List[int]], k: int) -> List[int]:
    n: int = len(grid)
    qem: int = n * n + 1

    # Iterate over each cell to find the minimal neighbor values for cells with value 1
    for row in range(n):
        for col in range(n):
            if grid[row][col] == 1:
                neighbors: List[int] = []
                if row > 0:
                    neighbors.append(grid[row - 1][col])
                if col > 0:
                    neighbors.append(grid[row][col - 1])
                if row < n - 1:
                    neighbors.append(grid[row + 1][col])
                if col < n - 1:
                    neighbors.append(grid[row][col + 1])
                if neighbors:
                    qem = min(qem, min(neighbors))

    result: List[int] = []
    for i in range(k):
        result.append(1 if i % 2 == 0 else qem)

    return result