from math import inf

class Solution:
    def maxScore(self, grid):
        a1 = len(grid)
        a2 = len(grid[0])

        def initList(x, y):
            return [[inf for _ in range(y)] for _ in range(x)]

        def minValue(p, q):
            return p if p < q else q

        def maxValue(p, q):
            return p if p > q else q

        b1 = initList(a1, a2)
        b1[0][0] = grid[0][0]

        y1 = 1
        while y1 < a2:
            b1[0][y1] = minValue(b1[0][y1 - 1], grid[0][y1])
            y1 += 1

        x1 = 1
        while x1 < a1:
            b1[x1][0] = minValue(b1[x1 - 1][0], grid[x1][0])
            x1 += 1

        x2 = 1
        maxTemp = -inf
        while x2 < a1:
            y2 = 1
            while y2 < a2:
                b1[x2][y2] = minValue(b1[x2 - 1][y2], b1[x2][y2 - 1])
                val1 = grid[x2][y2]
                val2 = b1[x2][y2]
                diffVal = val1 - val2
                maxTemp = maxValue(maxTemp, diffVal)
                y2 += 1
            x2 += 1

        return maxTemp