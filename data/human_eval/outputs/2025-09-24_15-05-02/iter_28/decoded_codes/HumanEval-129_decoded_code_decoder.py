from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    n: int = len(grid)
    val: int = n * n + 1

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                temp: List[int] = []
                if i != 0:
                    temp.append(grid[i - 1][j])
                if j != 0:
                    temp.append(grid[i][j - 1])
                if i != n - 1:
                    temp.append(grid[i + 1][j])
                if j != n - 1:
                    temp.append(grid[i][j + 1])
                if temp:
                    local_min = min(temp)
                    if local_min < val:
                        val = local_min

    ans: List[int] = []
    for i in range(k):
        ans.append(1 if i % 2 == 0 else val)

    return ans