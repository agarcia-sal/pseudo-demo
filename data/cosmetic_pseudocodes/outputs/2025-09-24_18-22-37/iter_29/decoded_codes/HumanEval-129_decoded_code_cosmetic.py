from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    n = len(grid)
    minimal_value = (n * n) + 1

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                neighbors = []
                if i > 0:
                    neighbors.append(grid[i - 1][j])
                if j > 0:
                    neighbors.append(grid[i][j - 1])
                if i < n - 1:
                    neighbors.append(grid[i + 1][j])
                if j < n - 1:
                    neighbors.append(grid[i][j + 1])

                if neighbors:
                    minimal_value = min(neighbors)

    result_sequence: List[int] = []
    for idx in range(k):
        if idx % 2 == 0:
            result_sequence.append(1)
        else:
            result_sequence.append(minimal_value)

    return result_sequence