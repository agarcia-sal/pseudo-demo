class Solution:
    def maxScore(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        dp = [None] * rows
        max_score = float('-inf')
        r = 0

        while r < rows:
            if r == 0:
                c = 0
                dp[0] = [float('inf')] * cols
                dp[0][0] = grid[0][0]
                while c < cols - 1:
                    dp[0][c + 1] = min(dp[0][c], grid[0][c + 1])
                    c += 1
            else:
                dp[r] = [float('inf')] * cols

                def Min(a, b):
                    return a if a < b else b

                dp[r][0] = Min(dp[r - 1][0], grid[r][0])
                x = 1
                while x < cols:
                    dp[r][x] = Min(dp[r][x - 1], grid[r][x])
                    x += 1

                z = 1
                while z < cols:
                    dp[r][z] = min(dp[r - 1][z], dp[r][z - 1])
                    difference = grid[r][z] - dp[r][z]
                    if difference > max_score:
                        max_score = difference
                    z += 1
            r += 1

        return max_score