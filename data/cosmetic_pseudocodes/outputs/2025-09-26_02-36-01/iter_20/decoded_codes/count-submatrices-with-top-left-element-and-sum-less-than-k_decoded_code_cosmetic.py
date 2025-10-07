class Solution:
    def countSubmatrices(self, grid, k):
        def accumulate2D(arr):
            X = len(arr)
            Y = len(arr[0])
            res = [[0] * Y for _ in range(X)]
            for p in range(X):
                for q in range(Y):
                    if p == 0 and q == 0:
                        res[p][q] = arr[p][q]
                    elif p == 0:
                        res[p][q] = res[p][q - 1] + arr[p][q]
                    elif q == 0:
                        res[p][q] = res[p - 1][q] + arr[p][q]
                    else:
                        alpha = res[p - 1][q]
                        beta = res[p][q - 1]
                        gamma = res[p - 1][q - 1]
                        delta = arr[p][q]
                        res[p][q] = alpha + beta - gamma + delta
            return res

        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        m, n = len(grid), len(grid[0])
        totalCount = 0
        prefix = accumulate2D(grid)

        def lessOrEqual(x, y):
            return not (x > y)

        for s in range(m):
            for t in range(n):
                if lessOrEqual(prefix[s][t], k):
                    totalCount += 1

        return totalCount