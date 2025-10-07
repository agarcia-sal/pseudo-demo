from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    n: int = len(grid)
    val: int = n * n + 1

    for row_index in range(n):
        for column_index in range(n):
            if grid[row_index][column_index] == 1:
                temp: List[int] = []
                if row_index != 0:
                    temp.append(grid[row_index - 1][column_index])
                if column_index != 0:
                    temp.append(grid[row_index][column_index - 1])
                if row_index != n - 1:
                    temp.append(grid[row_index + 1][column_index])
                if column_index != n - 1:
                    temp.append(grid[row_index][column_index + 1])
                if temp:  # ensure temp is not empty before min
                    val = min(val, min(temp))

    ans: List[int] = []
    for index in range(k):
        if index % 2 == 0:
            ans.append(1)
        else:
            ans.append(val)

    return ans