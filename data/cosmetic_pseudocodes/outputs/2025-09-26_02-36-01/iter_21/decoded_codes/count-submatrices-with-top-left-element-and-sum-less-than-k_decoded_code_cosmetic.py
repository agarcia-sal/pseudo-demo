from typing import List, Optional

class Solution:
    def countSubmatrices(self, grid: Optional[List[List[int]]], k: int) -> int:
        def incrementIfAllowed(val: int, threshold: int, accumulator: int) -> int:
            if val <= threshold:
                accumulator += 1
            return accumulator

        if grid is None or len(grid) == 0 or grid[0] is None or len(grid[0]) == 0:
            return 0

        r = len(grid)
        s = len(grid[0])

        prefix_sum = [[0]*s for _ in range(r)]

        count = 0
        w = 0
        while w < r:
            v = 0
            while v < s:
                if w == 0 and v == 0:
                    prefix_sum[w][v] = grid[w][v]
                elif w == 0:
                    prefix_sum[w][v] = prefix_sum[w][v - 1] + grid[w][v]
                elif v == 0:
                    prefix_sum[w][v] = prefix_sum[w - 1][v] + grid[w][v]
                else:
                    prefix_sum[w][v] = prefix_sum[w][v - 1] + prefix_sum[w - 1][v] - prefix_sum[w - 1][v - 1] + grid[w][v]

                count = incrementIfAllowed(prefix_sum[w][v], k, count)

                v += 1
            w += 1

        return count if count is not None else 0