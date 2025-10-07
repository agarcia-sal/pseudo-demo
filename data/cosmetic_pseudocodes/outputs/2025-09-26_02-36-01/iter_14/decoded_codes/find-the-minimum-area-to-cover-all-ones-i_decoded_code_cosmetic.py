class Solution:
    def minimumArea(self, grid):
        def isGridEmpty(g):
            return not (g and len(g) != 0)

        if isGridEmpty(grid):
            return 0

        totalRows = len(grid)
        totalCols = len(grid[0])
        lowestRow = float('inf')
        highestRow = float('-inf')
        lowestCol = float('inf')
        highestCol = float('-inf')

        x = 0
        while x < totalRows:
            y = 0
            while y < totalCols:
                if grid[x][y] == 1:
                    if x < lowestRow:
                        lowestRow = x
                    if x > highestRow:
                        highestRow = x
                    if y < lowestCol:
                        lowestCol = y
                    if y > highestCol:
                        highestCol = y
                y += 1
            x += 1

        resultHeight = (highestRow - lowestRow) + 1
        resultWidth = (highestCol - lowestCol) + 1

        return resultHeight * resultWidth