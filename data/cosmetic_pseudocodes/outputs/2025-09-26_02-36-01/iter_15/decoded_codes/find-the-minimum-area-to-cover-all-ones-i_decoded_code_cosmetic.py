class Solution:
    def minimumArea(self, grid):
        if not grid or not grid[0]:
            return 0

        a, b = len(grid), len(grid[0])
        c, d = float('inf'), float('-inf')  # min and max row indices
        e, f = float('inf'), float('-inf')  # min and max column indices

        for g in range(a):
            for h in range(b):
                if grid[g][h] == 1:
                    if c > g:
                        c = g
                    if d < g:
                        d = g
                    if e > h:
                        e = h
                    if f < h:
                        f = h

        height = (d - c) + 1
        width = (f - e) + 1
        return height * width