class Solution:
    def numberOfSubmatrices(self, grid):
        if not (len(grid) > 0 and len(grid[0]) > 0):
            return 0

        a = len(grid)
        b = len(grid[0])
        c = a + 1
        d = b + 1
        e = [[[0, 0] for _ in range(d)] for __ in range(c)]

        for h in range(1, c):
            for i in range(1, d):
                v0 = e[h][i - 1][0]
                v1 = e[h - 1][i][0]
                v2 = e[h - 1][i - 1][0]
                e[h][i][0] = v0 + v1 - v2

                w0 = e[h][i - 1][1]
                w1 = e[h - 1][i][1]
                w2 = e[h - 1][i - 1][1]
                e[h][i][1] = w0 + w1 - w2

                p = grid[h - 1][i - 1]
                if p == 'X':
                    e[h][i][0] += 1
                elif p == 'Y':
                    e[h][i][1] += 1

        m = 0
        for n in range(1, c):
            for o in range(1, d):
                s = e[n][o][0]
                t = e[n][o][1]
                if s > 0 and s == t:
                    m += 1
        return m