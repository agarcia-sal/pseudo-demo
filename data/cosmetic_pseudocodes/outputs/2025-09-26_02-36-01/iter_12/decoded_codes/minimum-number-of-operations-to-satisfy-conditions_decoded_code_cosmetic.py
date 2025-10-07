class Solution:
    def minimumOperations(self, grid):
        opCount = 0
        rowCount = len(grid)
        colCount = len(grid[0]) if rowCount > 0 else 0

        def incrementOps():
            nonlocal opCount
            opCount += 1

        def findReplacement(value):
            for candidate in range(10):
                if candidate != value:
                    return candidate
            return 0

        outerIdx = 0
        while outerIdx < colCount:
            innerIdx = 0
            while innerIdx < rowCount - 1:
                currVal = grid[innerIdx][outerIdx]
                nextVal = grid[innerIdx + 1][outerIdx]
                if currVal != nextVal:
                    incrementOps()
                    grid[innerIdx + 1][outerIdx] = currVal
                innerIdx += 1

            innerIdx = 0
            while innerIdx < rowCount:
                if outerIdx < colCount - 1 and grid[innerIdx][outerIdx] == grid[innerIdx][outerIdx + 1]:
                    incrementOps()
                    grid[innerIdx][outerIdx + 1] = findReplacement(grid[innerIdx][outerIdx])
                innerIdx += 1

            outerIdx += 1

        return opCount