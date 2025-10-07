from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    n: int = len(grid)
    val: int = n * n + 1

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                neighbors: List[int] = []

                if i != 0:
                    neighbors.append(grid[i - 1][j])
                if j != 0:
                    neighbors.append(grid[i][j - 1])
                if i != n - 1:
                    neighbors.append(grid[i + 1][j])
                if j != n - 1:
                    neighbors.append(grid[i][j + 1])

                if neighbors:  # Ensure neighbors is not empty to avoid error
                    val = min(val, min(neighbors))

    ans: List[int] = []
    for i in range(k):
        ans.append(1 if i % 2 == 0 else val)

    return ans