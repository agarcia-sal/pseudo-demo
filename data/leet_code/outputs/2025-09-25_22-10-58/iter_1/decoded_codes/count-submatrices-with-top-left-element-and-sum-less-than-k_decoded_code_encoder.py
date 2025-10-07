class Solution:
    def countSubmatrices(self, grid, k):
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        prefix_sum = [[0] * n for _ in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    prefix_sum[i][j] = grid[i][j]
                elif i == 0:
                    prefix_sum[i][j] = prefix_sum[i][j - 1] + grid[i][j]
                elif j == 0:
                    prefix_sum[i][j] = prefix_sum[i - 1][j] + grid[i][j]
                else:
                    prefix_sum[i][j] = (
                        prefix_sum[i - 1][j]
                        + prefix_sum[i][j - 1]
                        - prefix_sum[i - 1][j - 1]
                        + grid[i][j]
                    )
                if prefix_sum[i][j] <= k:
                    count += 1
        return count