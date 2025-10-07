from math import inf

class Solution:
    def maxScore(self, grid):
        m = len(grid)
        n = len(grid[0]) if m > 0 else 0
        dp = [[inf] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        max_score = -inf

        for j in range(1, n):
            dp[0][j] = min(dp[0][j-1], grid[0][j])

        for i in range(1, m):
            dp[i][0] = min(dp[i-1][0], grid[i][0])

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1])
                score = grid[i][j] - dp[i][j]
                if score > max_score:
                    max_score = score

        return max_score