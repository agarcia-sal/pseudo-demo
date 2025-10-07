from typing import List, Optional

class Solution:
    def countSubmatrices(self, grid: Optional[List[List[int]]], k: int) -> int:
        if not grid or not grid[0]:
            return 0

        x1, y1 = len(grid), len(grid[0])
        ps = [[0] * y1 for _ in range(x1)]
        res = 0

        for a in range(x1):
            for b in range(y1):
                if a == 0 and b == 0:
                    ps[a][b] = grid[a][b]
                elif a == 0:
                    ps[a][b] = ps[a][b - 1] + grid[a][b]
                elif b == 0:
                    ps[a][b] = ps[a - 1][b] + grid[a][b]
                else:
                    ps[a][b] = ps[a - 1][b] + ps[a][b - 1] - ps[a - 1][b - 1] + grid[a][b]

                if ps[a][b] <= k:
                    res += 1

        return res