from math import inf
from typing import List

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        min_row = inf
        max_row = -inf
        min_col = inf
        max_col = -inf

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    if i < min_row:
                        min_row = i
                    if i > max_row:
                        max_row = i
                    if j < min_col:
                        min_col = j
                    if j > max_col:
                        max_col = j

        if min_row == inf:  # No 1's found
            return 0

        height = max_row - min_row + 1
        width = max_col - min_col + 1
        return height * width