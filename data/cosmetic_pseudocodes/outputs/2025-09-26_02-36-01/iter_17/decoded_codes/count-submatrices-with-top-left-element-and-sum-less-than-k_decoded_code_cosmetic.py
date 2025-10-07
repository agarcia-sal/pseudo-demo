class Solution:
    def countSubmatrices(self, grid, k):
        if not grid or not grid[0]:
            return 0

        w = len(grid)
        x = len(grid[0])

        v = [[0] * x for _ in range(w)]
        y = 0

        for u in range(w):
            for r in range(x):
                if u == 0 and r == 0:
                    v[u][r] = grid[u][r]
                elif u == 0:
                    v[u][r] = v[u][r - 1] + grid[u][r]
                elif r == 0:
                    v[u][r] = v[u - 1][r] + grid[u][r]
                else:
                    v[u][r] = v[u - 1][r] + v[u][r - 1] - v[u - 1][r - 1] + grid[u][r]

                if v[u][r] <= k:
                    y += 1

        return y