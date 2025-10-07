class Solution:
    def numberOfSubmatrices(self, grid):
        def helper(iIndex, jIndex, totalRows, totalCols, prefixMatrix):
            if iIndex > totalRows:
                return
            elif jIndex > totalCols:
                helper(iIndex + 1, 1, totalRows, totalCols, prefixMatrix)
            else:
                upperLeftX = prefixMatrix[iIndex - 1][jIndex][0]
                leftX = prefixMatrix[iIndex][jIndex - 1][0]
                upperLeftXMinus = prefixMatrix[iIndex - 1][jIndex - 1][0]
                upperLeftY = prefixMatrix[iIndex - 1][jIndex][1]
                leftY = prefixMatrix[iIndex][jIndex - 1][1]
                upperLeftYMinus = prefixMatrix[iIndex - 1][jIndex - 1][1]

                gridRow = grid[iIndex - 1]
                gridValue = gridRow[jIndex - 1]

                prefixMatrix[iIndex][jIndex][0] = upperLeftX + leftX - upperLeftXMinus
                prefixMatrix[iIndex][jIndex][1] = upperLeftY + leftY - upperLeftYMinus

                if gridValue == 'X':
                    prefixMatrix[iIndex][jIndex][0] += 1
                elif gridValue == 'Y':
                    prefixMatrix[iIndex][jIndex][1] += 1

                helper(iIndex, jIndex + 1, totalRows, totalCols, prefixMatrix)

        if not grid or not grid[0]:
            return 0

        totalRowCount = len(grid)
        colCount = len(grid[0])

        prefixSumArray = [[[0, 0] for _ in range(colCount + 1)] for __ in range(totalRowCount + 1)]

        helper(1, 1, totalRowCount, colCount, prefixSumArray)

        accumulator = 0
        for p in range(1, totalRowCount + 1):
            for r in range(1, colCount + 1):
                xNum = prefixSumArray[p][r][0]
                yNum = prefixSumArray[p][r][1]
                if xNum > 0 and not (xNum != yNum):
                    accumulator += 1

        return accumulator