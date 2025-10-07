class Solution:
    def numberOfSubmatrices(self, grid):
        if not grid or not grid[0]:
            return 0

        alpha = len(grid)
        beta = len(grid[0])

        # Initialize gamma as a (alpha+2) x (beta+2) matrix with [0,0] pairs
        gamma = [[[0, 0] for _ in range(beta + 2)] for __ in range(alpha + 2)]

        def zeta(r, c):
            return gamma[r-1][c][0] + gamma[r][c-1][0] - gamma[r-1][c-1][0]

        def eta(r, c):
            return gamma[r-1][c][1] + gamma[r][c-1][1] - gamma[r-1][c-1][1]

        def increment_counts(r, c):
            val = grid[r-1][c-1]
            if val == 'X':
                gamma[r][c][0] += 1
            elif val == 'Y':
                gamma[r][c][1] += 1

        m = 1
        while m <= alpha:
            n = 1
            while n <= beta:
                gamma[m][n][0] = zeta(m, n)
                gamma[m][n][1] = eta(m, n)
                increment_counts(m, n)
                n += 1
            m += 1

        total = 0
        q = 1
        while q <= alpha:
            w = 1
            while w <= beta:
                u = gamma[q][w][0]
                v = gamma[q][w][1]
                if u > 0 and u == v:
                    total += 1
                w += 1
            q += 1

        return total