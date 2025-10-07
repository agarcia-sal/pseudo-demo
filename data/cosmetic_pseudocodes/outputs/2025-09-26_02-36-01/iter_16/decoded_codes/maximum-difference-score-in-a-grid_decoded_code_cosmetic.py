class Solution:
    def maxScore(self, grid):
        m = len(grid)
        n = len(grid[0])
        dp = [[float('inf')] * n for _ in range(m)]
        dp[0][0] = grid[0][0]

        # Initialize first row
        for j in range(1, n):
            dp[0][j] = min(dp[0][j - 1], grid[0][j])

        # Initialize first column
        for i in range(1, m):
            dp[i][0] = min(dp[i - 1][0], grid[i][0])

        max_diff = float('-inf')

        # Fill the dp table and compute max diff
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j])
                diff = grid[i][j] - dp[i][j]
                if diff > max_diff:
                    max_diff = diff

        return max_diff