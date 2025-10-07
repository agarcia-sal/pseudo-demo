from math import inf

class Solution:
    def maxScore(self, grid):
        a = len(grid)
        b = len(grid[0])
        c = [[inf] * b for _ in range(a)]
        c[0][0] = grid[0][0]
        d = float('-inf')

        e = 1
        while e < b:
            if c[0][e - 1] < grid[0][e]:
                c[0][e] = c[0][e - 1]
            else:
                c[0][e] = grid[0][e]
            e += 1

        f = 1
        while f < a:
            if c[f - 1][0] < grid[f][0]:
                c[f][0] = c[f - 1][0]
            else:
                c[f][0] = grid[f][0]
            f += 1

        g = 1
        while g < a:
            h = 1
            while h < b:
                if c[g][h - 1] < c[g - 1][h]:
                    c[g][h] = c[g][h - 1]
                else:
                    c[g][h] = c[g - 1][h]
                i = grid[g][h] - c[g][h]
                if i > d:
                    d = i
                h += 1
            g += 1

        return d