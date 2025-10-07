from typing import List

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        operations = 0

        for j in range(n):
            for i in range(m - 1):
                if grid[i][j] != grid[i + 1][j]:
                    operations += 1
                    grid[i + 1][j] = grid[i][j]

            if j < n - 1:
                for i in range(m):
                    if grid[i][j] == grid[i][j + 1]:
                        operations += 1
                        for val in range(10):
                            if val != grid[i][j]:
                                grid[i][j + 1] = val
                                break

        return operations