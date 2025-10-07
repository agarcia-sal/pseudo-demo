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
                    min_temp = temp[0]
                    for index in range(1, len(temp)):
                        if temp[index] < min_temp:
                            min_temp = temp[index]
                    val = min_temp
    ans: List[int] = []
    for i in range(k):
        if i % 2 == 0:
            ans.append(1)
        else:
            ans.append(val)
    return ans