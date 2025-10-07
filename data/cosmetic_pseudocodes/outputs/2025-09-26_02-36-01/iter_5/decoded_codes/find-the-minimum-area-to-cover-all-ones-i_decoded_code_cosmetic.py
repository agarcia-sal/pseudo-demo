from math import inf

class Solution:
    def minimumArea(self, grid):
        if not grid or not grid[0]:
            return 0

        upperBoundRow = inf
        lowerBoundRow = -inf
        leftBoundCol = inf
        rightBoundCol = -inf

        def scanRows(rowIndex):
            nonlocal upperBoundRow, lowerBoundRow, leftBoundCol, rightBoundCol
            if rowIndex > len(grid) - 1:
                return
            def scanCols(colIndex):
                nonlocal upperBoundRow, lowerBoundRow, leftBoundCol, rightBoundCol
                if colIndex > len(grid[0]) - 1:
                    return
                currentElem = grid[rowIndex][colIndex]
                if currentElem == 1:
                    if upperBoundRow > rowIndex:
                        upperBoundRow = rowIndex
                    if lowerBoundRow < rowIndex:
                        lowerBoundRow = rowIndex
                    if leftBoundCol > colIndex:
                        leftBoundCol = colIndex
                    if rightBoundCol < colIndex:
                        rightBoundCol = colIndex
                scanCols(colIndex + 1)
            scanCols(0)
            scanRows(rowIndex + 1)

        scanRows(0)

        if upperBoundRow == inf or leftBoundCol == inf:
            return 0  # no '1' found

        rectHeight = (lowerBoundRow - upperBoundRow) + 1
        rectWidth = (rightBoundCol - leftBoundCol) + 1
        resultArea = rectHeight * rectWidth

        return resultArea