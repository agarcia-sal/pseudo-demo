from typing import List

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        sums = [[0] * cols for _ in range(rows)]
        total = 0
        for x in range(rows):
            for y in range(cols):
                if x == 0 and y == 0:
                    sums[x][y] = grid[x][y]
                elif x == 0:
                    sums[x][y] = sums[x][y - 1] + grid[x][y]
                elif y == 0:
                    sums[x][y] = sums[x - 1][y] + grid[x][y]
                else:
                    sums[x][y] = sums[x][y - 1] + sums[x - 1][y] - sums[x - 1][y - 1] + grid[x][y]
                if sums[x][y] <= k:
                    total += 1
        return total