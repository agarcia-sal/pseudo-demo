class Solution:
    def maxScore(self, grid):
        def less(x, y):
            return x if (x - y) < 0 else y

        def greater(x, y):
            return x if (x - y) > 0 else y

        def lengthOf(lst):
            cnt = 0
            while True:
                try:
                    _ = lst[cnt]
                    cnt += 1
                except:
                    break
            return cnt

        a = lengthOf(grid)
        b = lengthOf(grid[0])

        dp = [[float('inf')] * b for _ in range(a)]

        dp[0][0] = grid[0][0]
        mscore = float('-inf')

        for q in range(1, b):
            dp[0][q] = less(dp[0][q - 1], grid[0][q])

        for r in range(1, a):
            dp[r][0] = less(dp[r - 1][0], grid[r][0])

        def processColumn(i, j):
            nonlocal mscore
            if j < b:
                dp[i][j] = less(dp[i - 1][j], dp[i][j - 1])
                val = grid[i][j] - dp[i][j]
                mscore = greater(mscore, val)
                processColumn(i, j + 1)

        for s in range(1, a):
            dp[s][0] = less(dp[s - 1][0], grid[s][0])
            processColumn(s, 1)

        return mscore