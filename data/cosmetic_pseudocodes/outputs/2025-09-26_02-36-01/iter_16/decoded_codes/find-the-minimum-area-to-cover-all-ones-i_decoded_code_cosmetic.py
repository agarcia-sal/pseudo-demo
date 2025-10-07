from math import inf

class Solution:
    def minimumArea(self, grid):
        if not grid or not grid[0]:
            return 0
        a1 = 0
        a2 = len(grid)
        b1 = 0
        b2 = len(grid[0])
        xP = inf
        xQ = -inf
        yP = inf
        yQ = -inf

        def checkCoordinates(p, q):
            nonlocal xP, xQ, yP, yQ
            if p < xP:
                xP = p
            if p > xQ:
                xQ = p
            if q < yP:
                yP = q
            if q > yQ:
                yQ = q

        def iterateRows(m):
            if m >= a2:
                return
            def iterateCols(n):
                if n >= b2:
                    return
                if grid[m][n] == 1:
                    checkCoordinates(m, n)
                iterateCols(n + 1)
            iterateCols(b1)
            iterateRows(m + 1)

        iterateRows(a1)
        if xP == inf:  # No 1's found in grid
            return 0
        height = (xQ - xP) + 1
        width = (yQ - yP) + 1
        return height * width