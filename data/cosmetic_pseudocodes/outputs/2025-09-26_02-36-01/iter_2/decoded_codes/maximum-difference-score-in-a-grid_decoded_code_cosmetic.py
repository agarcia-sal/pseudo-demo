from math import inf

class Solution:
    def maxScore(self, grid):
        height = len(grid)
        width = len(grid[0])
        dp = [[inf] * width for _ in range(height)]
        dp[0][0] = grid[0][0]
        best_score = float('-inf')

        for col_idx in range(1, width):
            dp[0][col_idx] = min(dp[0][col_idx - 1], grid[0][col_idx])

        for row_idx in range(1, height):
            dp[row_idx][0] = min(dp[row_idx - 1][0], grid[row_idx][0])

        for r in range(1, height):
            for c in range(1, width):
                current_min = min(dp[r - 1][c], dp[r][c - 1])
                dp[r][c] = current_min
                current_diff = grid[r][c] - dp[r][c]
                if best_score < current_diff:
                    best_score = current_diff

        return best_score