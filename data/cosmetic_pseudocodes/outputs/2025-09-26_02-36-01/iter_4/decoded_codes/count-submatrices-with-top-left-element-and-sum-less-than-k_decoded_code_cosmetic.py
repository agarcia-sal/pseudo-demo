class Solution:
    def countSubmatrices(self, grid, k):
        if not grid or not grid[0]:
            return 0
        totalRows = len(grid)
        totalCols = len(grid[0])
        prefixSum = [[0] * totalCols for _ in range(totalRows)]
        resultCounter = 0

        for rowIndex in range(totalRows):
            for colIndex in range(totalCols):
                if rowIndex == 0 and colIndex == 0:
                    prefixSum[rowIndex][colIndex] = grid[rowIndex][colIndex]
                elif rowIndex == 0:
                    prefixSum[rowIndex][colIndex] = prefixSum[rowIndex][colIndex - 1] + grid[rowIndex][colIndex]
                elif colIndex == 0:
                    prefixSum[rowIndex][colIndex] = prefixSum[rowIndex - 1][colIndex] + grid[rowIndex][colIndex]
                else:
                    prefixSum[rowIndex][colIndex] = (
                        prefixSum[rowIndex - 1][colIndex] +
                        prefixSum[rowIndex][colIndex - 1] -
                        prefixSum[rowIndex - 1][colIndex - 1] +
                        grid[rowIndex][colIndex]
                    )
                if prefixSum[rowIndex][colIndex] <= k:
                    resultCounter += 1
        return resultCounter