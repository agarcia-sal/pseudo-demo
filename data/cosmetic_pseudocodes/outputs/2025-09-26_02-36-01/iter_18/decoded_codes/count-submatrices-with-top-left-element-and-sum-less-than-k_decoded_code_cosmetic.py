class Solution:
    def countSubmatrices(self, grid, k):
        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])

        prefix = [[0] * n for _ in range(m)]
        count = 0

        # Build prefix sum matrix and count prefix sums <= k
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    prefix[i][j] = grid[i][j]
                elif i == 0:
                    prefix[i][j] = prefix[i][j - 1] + grid[i][j]
                elif j == 0:
                    prefix[i][j] = prefix[i - 1][j] + grid[i][j]
                else:
                    prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + grid[i][j]
                if prefix[i][j] <= k:
                    count += 1

        return count