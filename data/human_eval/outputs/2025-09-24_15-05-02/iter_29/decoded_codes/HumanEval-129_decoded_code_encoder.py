from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    n: int = len(grid)
    val: int = n * n + 1
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                temporary_list: List[int] = []
                if i != 0:
                    temporary_list.append(grid[i - 1][j])
                if j != 0:
                    temporary_list.append(grid[i][j - 1])
                if i != n - 1:
                    temporary_list.append(grid[i + 1][j])
                if j != n - 1:
                    temporary_list.append(grid[i][j + 1])
                if temporary_list:
                    val = min(val, min(temporary_list))
    ans: List[int] = []
    for index in range(k):
        if index % 2 == 0:
            ans.append(1)
        else:
            ans.append(val)
    return ans