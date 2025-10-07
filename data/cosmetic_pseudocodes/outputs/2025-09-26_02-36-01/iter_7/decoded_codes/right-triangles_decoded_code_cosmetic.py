from typing import List

class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0]) if m > 0 else 0
        accum_result = 0
        outer_idx = 0
        while outer_idx <= m - 1:
            inner_idx = 0
            while inner_idx <= n - 1:
                if grid[outer_idx][inner_idx] == 1:
                    horizontal_total = 0
                    col_iter = 0
                    while col_iter <= n - 1:
                        if col_iter != inner_idx:
                            horizontal_total += grid[outer_idx][col_iter]
                        col_iter += 1

                    vertical_total = 0
                    row_iter = 0
                    while row_iter <= m - 1:
                        if row_iter != outer_idx:
                            vertical_total += grid[row_iter][inner_idx]
                        row_iter += 1

                    accum_result += horizontal_total * vertical_total
                inner_idx += 1
            outer_idx += 1
        return accum_result