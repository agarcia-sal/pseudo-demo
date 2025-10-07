class Solution:
    def countSubmatrices(self, grid, k):
        resultCounter = 0
        if not (grid and grid[0]):
            return resultCounter

        rowCount, colCount = len(grid), len(grid[0])
        aggregatedSums = [[0] * colCount for _ in range(rowCount)]

        def computeCell(r, c):
            if r == 0 and c == 0:
                return grid[r][c]
            elif r == 0:
                return aggregatedSums[r][c - 1] + grid[r][c]
            elif c == 0:
                return aggregatedSums[r - 1][c] + grid[r][c]
            else:
                return aggregatedSums[r - 1][c] + aggregatedSums[r][c - 1] - aggregatedSums[r - 1][c - 1] + grid[r][c]

        def rowIter(accRow):
            nonlocal resultCounter
            if accRow == rowCount:
                return
            def colIter(accCol):
                nonlocal resultCounter
                if accCol == colCount:
                    return
                cellSum = computeCell(accRow, accCol)
                aggregatedSums[accRow][accCol] = cellSum
                if cellSum <= k:
                    resultCounter += 1
                colIter(accCol + 1)
            colIter(0)
            rowIter(accRow + 1)

        rowIter(0)
        return resultCounter