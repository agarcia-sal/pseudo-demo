class Solution:
    def numberOfRightTriangles(self, grid):
        totalTriangles = 0
        maxRowIndex = len(grid) - 1
        maxColIndex = len(grid[0]) - 1 if grid else -1

        def sumRowExceptIndex(arr, excludedIndex):
            return sum(arr[i] for i in range(len(arr)) if i != excludedIndex)

        def sumColExceptIndex(matrix, colIndex, excludedRow):
            return sum(matrix[r][colIndex] for r in range(len(matrix)) if r != excludedRow)

        def processCell(rowIdx, colIdx, gridData):
            if gridData[rowIdx][colIdx] == 1:
                countAlongRow = sumRowExceptIndex(gridData[rowIdx], colIdx)
                countAlongCol = sumColExceptIndex(gridData, colIdx, rowIdx)
                return countAlongRow * countAlongCol
            else:
                return 0

        def iterateRows(rIndex):
            if rIndex > maxRowIndex:
                return 0
            return iterateCols(rIndex, 0) + iterateRows(rIndex + 1)

        def iterateCols(rIdx, cIdx):
            if cIdx > maxColIndex:
                return 0
            return processCell(rIdx, cIdx, grid) + iterateCols(rIdx, cIdx + 1)

        totalTriangles = iterateRows(0)
        return totalTriangles