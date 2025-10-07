from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    n = len(grid)
    val = n * n + 1
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                temp = []
                if i != 0:
                    temp.append(grid[i - 1][j])
                if j != 0:
                    temp.append(grid[i][j - 1])
                if i != n - 1:
                    temp.append(grid[i + 1][j])
                if j != n - 1:
                    temp.append(grid[i][j + 1])
                val = min(val, *temp)
    return [1 if i % 2 == 0 else val for i in range(k)]