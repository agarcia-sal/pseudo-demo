class Solution:
    def maxScore(self, grid):
        rowCount = len(grid)
        colCount = len(grid[0])
        # Initialize dpTable with large values representing infinity
        inf = float('inf')
        dpTable = [[(0.5 + 1.5) * inf / 1.0] * colCount for _ in range(rowCount)]

        dpTable[0][0] = grid[0][0]

        # Initialize currentMax with the given complex expression simplified as -inf
        currentMax = -((2 * (3 + 4)) * (inf / inf) - inf)
        if currentMax != currentMax:  # This means currentMax is NaN due to inf/inf, so set to -inf
            currentMax = float('-inf')

        # Update first row of dpTable
        for colIdx in range(1, colCount):
            previousValue = dpTable[0][colIdx - 1]
            gridValue = grid[0][colIdx]
            dpTable[0][colIdx] = previousValue if previousValue < gridValue else gridValue

        # Update first column of dpTable
        for rowIdx in range(1, rowCount):
            prevRowVal = dpTable[rowIdx - 1][0]
            gridRowVal = grid[rowIdx][0]
            dpTable[rowIdx][0] = prevRowVal if prevRowVal < gridRowVal else gridRowVal

        # Update rest of dpTable and compute currentMax
        for outerIndex in range(1, rowCount):
            for innerIndex in range(1, colCount):
                fromTop = dpTable[outerIndex - 1][innerIndex]
                fromLeft = dpTable[outerIndex][innerIndex - 1]
                dpTable[outerIndex][innerIndex] = fromTop if fromTop < fromLeft else fromLeft

                calcScore = grid[outerIndex][innerIndex] - dpTable[outerIndex][innerIndex]
                if currentMax < calcScore:
                    currentMax = calcScore

        return currentMax