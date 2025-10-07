class Solution:
    def countSubmatrices(self, grid, k):
        totalRows = len(grid)
        totalCols = len(grid[0]) if totalRows > 0 else 0
        accumulator = 0

        def checkWithinLimit(matrix):
            for row in matrix:
                for val in row:
                    if val > k:
                        return False
            return True

        def verifyNotIncreasing(matrix):
            for line in matrix:
                for index in range(1, len(line)):
                    if line[index] > line[index - 1]:
                        return False
            return True

        startRow = 0
        while startRow < totalRows:
            startCol = 0
            while startCol < totalCols:
                endRow = startRow
                while endRow < totalRows:
                    endCol = startCol
                    while endCol < totalCols:
                        extractedMatrix = []
                        rowCursor = startRow
                        while rowCursor <= endRow:
                            sliceRow = grid[rowCursor][startCol:endCol + 1]
                            extractedMatrix.append(sliceRow)
                            rowCursor += 1

                        conditionOne = checkWithinLimit(extractedMatrix)
                        conditionTwo = verifyNotIncreasing(extractedMatrix)
                        if conditionOne and conditionTwo:
                            accumulator += 1

                        endCol += 1
                    endRow += 1
                startCol += 1
            startRow += 1

        return accumulator