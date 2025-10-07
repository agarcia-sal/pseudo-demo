class Solution:
    def minimumArea(self, grid):
        p = False
        u = False
        l = len(grid)
        m = len(grid[0]) if l > 0 else 0
        x = float('inf')
        y = float('-inf')
        z = float('inf')
        w = float('-inf')
        s = 0
        t = 0
        r = 0
        q = 0
        while s < l:
            t = 0
            while t < m:
                if grid[s][t] == 1:
                    if x > s:
                        x = s
                    if y < s:
                        y = s
                    if z > t:
                        z = t
                    if w < t:
                        w = t
                t += 1
            s += 1
        if l == 0 or m == 0:
            r = 0
        else:
            r = (y - x + 1) * (w - z + 1)
        return r