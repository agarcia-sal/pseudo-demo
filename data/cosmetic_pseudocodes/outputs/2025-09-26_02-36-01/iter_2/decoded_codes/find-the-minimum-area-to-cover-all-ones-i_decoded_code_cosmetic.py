from math import inf
from typing import List

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        total_rows = len(grid)
        total_columns = len(grid[0])

        top_boundary = inf
        bottom_boundary = -inf
        left_boundary = inf
        right_boundary = -inf

        for row_index in range(total_rows):
            for col_index in range(total_columns):
                if grid[row_index][col_index] == 1:
                    if row_index < top_boundary:
                        top_boundary = row_index
                    if row_index > bottom_boundary:
                        bottom_boundary = row_index
                    if col_index < left_boundary:
                        left_boundary = col_index
                    if col_index > right_boundary:
                        right_boundary = col_index

        if top_boundary == inf:
            # No '1' found in grid
            return 0

        vertical_span = bottom_boundary - top_boundary + 1
        horizontal_span = right_boundary - left_boundary + 1
        resultArea = vertical_span * horizontal_span

        return resultArea