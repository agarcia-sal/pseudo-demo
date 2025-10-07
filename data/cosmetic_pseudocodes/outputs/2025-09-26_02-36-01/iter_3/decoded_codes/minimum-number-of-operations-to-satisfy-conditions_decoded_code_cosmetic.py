class Solution:
    def minimumOperations(self, grid):
        rowCount = len(grid)
        colCount = len(grid[0])
        opsCounter = 0

        colIndex = 0
        while colIndex < colCount:
            rowCursor = 0
            while rowCursor < rowCount - 1:
                currentVal = grid[rowCursor][colIndex]
                nextVal = grid[rowCursor + 1][colIndex]
                if currentVal != nextVal:
                    opsCounter += 1
                    grid[rowCursor + 1][colIndex] = currentVal
                rowCursor += 1

            checkRow = 0
            while checkRow < rowCount:
                if (colIndex < colCount - 1) and (grid[checkRow][colIndex] == grid[checkRow][colIndex + 1]):
                    opsCounter += 1
                    newValue = 0
                    while newValue <= 9:
                        if newValue != grid[checkRow][colIndex]:
                            grid[checkRow][colIndex + 1] = newValue
                            break
                        newValue += 1
                checkRow += 1

            colIndex += 1

        return opsCounter