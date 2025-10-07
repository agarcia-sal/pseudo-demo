import math

class Solution:
    def maxScore(self, grid):
        rowsCount = len(grid)
        colsCount = len(grid[0])

        def createInfinityRow(lengthVal):
            # Iteratively build a list of lengthVal filled with positive infinity
            return [math.inf] * lengthVal

        def buildDp(rowsLeft, dpAcc):
            # Recursively build dp matrix filled with infinity rows
            if rowsLeft == 0:
                return dpAcc
            newRow = createInfinityRow(colsCount)
            return buildDp(rowsLeft - 1, dpAcc + [newRow])

        dpMatrix = buildDp(rowsCount, [])
        dpMatrix[0][0] = grid[0][0]

        indexCol = 1
        while indexCol < colsCount:
            leftVal = dpMatrix[0][indexCol - 1]
            currentGridVal = grid[0][indexCol]
            dpMatrix[0][indexCol] = leftVal if leftVal < currentGridVal else currentGridVal
            indexCol += 1

        indexRow = 1
        while indexRow < rowsCount:
            topVal = dpMatrix[indexRow - 1][0]
            currentGridVal = grid[indexRow][0]
            dpMatrix[indexRow][0] = topVal if topVal < currentGridVal else currentGridVal
            indexRow += 1

        def processRow(colCursor, rowIdx, currMax):
            if colCursor == colsCount:
                return currMax
            fromTop = dpMatrix[rowIdx - 1][colCursor]
            fromLeft = dpMatrix[rowIdx][colCursor - 1]
            minVal = fromTop if fromTop <= fromLeft else fromLeft
            dpMatrix[rowIdx][colCursor] = minVal

            currentDiff = grid[rowIdx][colCursor] - dpMatrix[rowIdx][colCursor]
            updatedMax = currentDiff if currentDiff > currMax else currMax

            return processRow(colCursor + 1, rowIdx, updatedMax)

        def processAllRows(rIdx, currentMaxScore):
            if rIdx == rowsCount:
                return currentMaxScore
            maxAfterRow = processRow(1, rIdx, currentMaxScore)
            return processAllRows(rIdx + 1, maxAfterRow)

        finalMax = processAllRows(1, -math.inf)
        return finalMax