class Solution:
    def minimumOperations(self, grid):
        totalRows = len(grid)
        totalCols = len(grid[0])
        changeCount = 0

        def loopOne(col, row):
            nonlocal changeCount
            if row > totalRows - 2:
                return
            if grid[row][col] != grid[row + 1][col]:
                changeCount += 1
                grid[row + 1][col] = grid[row][col]
            loopOne(col, row + 1)

        def loopTwo(col, row):
            nonlocal changeCount
            if row > totalRows - 1:
                return
            if col < totalCols - 1:
                if grid[row][col] == grid[row][col + 1]:
                    changeCount += 1

                    def findReplacement(val):
                        if val > 9:
                            return
                        if val != grid[row][col]:
                            grid[row][col + 1] = val
                            return
                        findReplacement(val + 1)

                    findReplacement(0)
            loopTwo(col, row + 1)

        def outerLoop(col):
            if col > totalCols - 1:
                return
            loopOne(col, 0)
            loopTwo(col, 0)
            outerLoop(col + 1)

        outerLoop(0)

        return changeCount