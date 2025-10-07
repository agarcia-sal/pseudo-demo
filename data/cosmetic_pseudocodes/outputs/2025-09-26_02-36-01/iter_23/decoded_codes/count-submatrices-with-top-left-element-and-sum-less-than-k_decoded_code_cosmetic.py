class Solution:
    def countSubmatrices(self, grid, k):
        def innerCountMatrixRow(gridMatrix, limit, rowIndex, colIndex, prefixMat, totalCount):
            if colIndex >= len(gridMatrix[0]):
                return totalCount
            else:
                if rowIndex == 0 and colIndex == 0:
                    prefixMat[rowIndex][colIndex] = gridMatrix[rowIndex][colIndex]
                elif rowIndex == 0:
                    calcSum = prefixMat[rowIndex][colIndex - 1] + gridMatrix[rowIndex][colIndex]
                    prefixMat[rowIndex][colIndex] = calcSum
                elif colIndex == 0:
                    calcSum = prefixMat[rowIndex - 1][colIndex] + gridMatrix[rowIndex][colIndex]
                    prefixMat[rowIndex][colIndex] = calcSum
                else:
                    calcSum = (prefixMat[rowIndex][colIndex - 1]
                               + prefixMat[rowIndex - 1][colIndex]
                               - prefixMat[rowIndex - 1][colIndex - 1]
                               + gridMatrix[rowIndex][colIndex])
                    prefixMat[rowIndex][colIndex] = calcSum
                accSum = totalCount + 1 if prefixMat[rowIndex][colIndex] <= limit else totalCount
                return innerCountMatrixRow(gridMatrix, limit, rowIndex, colIndex + 1, prefixMat, accSum)

        def innerCountMatrixCol(gridMatrix, limit, currentRow, totalRows, prefixMat, countSoFar):
            if currentRow >= totalRows:
                return countSoFar
            else:
                newCount = innerCountMatrixRow(gridMatrix, limit, currentRow, 0, prefixMat, countSoFar)
                return innerCountMatrixCol(gridMatrix, limit, currentRow + 1, totalRows, prefixMat, newCount)

        if not grid or not grid[0]:
            return 0

        dimensionM = len(grid)
        dimensionN = len(grid[0])
        matrixPrefix = [[0] * dimensionN for _ in range(dimensionM)]
        return innerCountMatrixCol(grid, k, 0, dimensionM, matrixPrefix, 0)