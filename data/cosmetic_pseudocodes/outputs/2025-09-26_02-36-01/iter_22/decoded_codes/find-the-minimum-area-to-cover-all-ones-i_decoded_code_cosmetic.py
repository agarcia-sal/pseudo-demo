from math import inf

class Solution:
    def minimumArea(self, grid):
        if not grid or not grid[0]:
            return 0

        a1, a2 = len(grid), len(grid[0])
        uA, uB = inf, -inf
        uC, uD = inf, -inf

        for p in range(a1):
            for q in range(a2):
                if grid[p][q] == 1:
                    if uA > p:
                        uA = p
                    if uB < p:
                        uB = p
                    if uC > q:
                        uC = q
                    if uD < q:
                        uD = q

        if uA == inf:  # no 1 found
            return 0

        hgt = (uB - uA) + 1
        wid = (uD - uC) + 1
        return hgt * wid