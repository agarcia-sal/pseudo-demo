from typing import List

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        prefix_sum = [[0] * cols for _ in range(rows)]
        count = 0

        for row in range(rows):
            for col in range(cols):
                top_left = prefix_sum[row - 1][col - 1] if row > 0 and col > 0 else 0
                top = prefix_sum[row - 1][col] if row > 0 else 0
                left = prefix_sum[row][col - 1] if col > 0 else 0
                prefix_sum[row][col] = grid[row][col] + top + left - top_left

                if prefix_sum[row][col] <= k:
                    count += 1

        return count