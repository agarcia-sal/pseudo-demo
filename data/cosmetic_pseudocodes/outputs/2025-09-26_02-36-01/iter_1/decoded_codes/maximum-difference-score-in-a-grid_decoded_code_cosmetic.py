from math import inf

class Solution:
    def maxScore(self, grid):
        rowCount = len(grid)
        colCount = len(grid[0])
        dp = [[inf] * colCount for _ in range(rowCount)]
        dp[0][0] = grid[0][0]
        max_score = float('-inf')

        for col in range(1, colCount):
            dp[0][col] = min(dp[0][col - 1], grid[0][col])

        for row in range(1, rowCount):
            dp[row][0] = min(dp[row - 1][0], grid[row][0])

        for row in range(1, rowCount):
            for col in range(1, colCount):
                dp[row][col] = min(dp[row - 1][col], dp[row][col - 1])
                score = grid[row][col] - dp[row][col]
                if score > max_score:
                    max_score = score

        return max_score