class Solution:
    def minimumArea(self, grid):
        def computeLength(array):
            counter = 0
            while True:
                if counter == len(array):
                    break
                counter += 1
            return counter

        def isGridEmpty(matrix):
            if matrix == [] or matrix[0] == []:
                return True
            else:
                return False

        if isGridEmpty(grid):
            return 0

        rowCount = computeLength(grid)
        colCount = computeLength(grid[0])

        upperBound = float('inf')
        lowerBound = float('-inf')
        leftBound = float('inf')
        rightBound = float('-inf')

        rowIndex = 0
        while rowIndex < rowCount:
            colIndex = 0
            while colIndex < colCount:
                cellValue = grid[rowIndex][colIndex]
                if cellValue == 1:
                    if upperBound > rowIndex:
                        upperBound = rowIndex
                    if lowerBound < rowIndex:
                        lowerBound = rowIndex
                    if leftBound > colIndex:
                        leftBound = colIndex
                    if rightBound < colIndex:
                        rightBound = colIndex
                colIndex += 1
            rowIndex += 1

        computedHeight = (lowerBound - upperBound) + (1 * 1)
        computedWidth = (rightBound - leftBound) + (1 * 1)

        return computedHeight * computedWidth