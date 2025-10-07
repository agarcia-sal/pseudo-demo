class Solution:
    def minimumOperations(self, grid):
        rowCount = len(grid)
        colCount = len(grid[0])
        totalOps = 0

        colIndex = 0
        while colIndex < colCount:
            rowIndex = 0
            while rowIndex < rowCount - 1:
                currentVal = grid[rowIndex][colIndex]
                nextVal = grid[rowIndex + 1][colIndex]
                if currentVal != nextVal:
                    totalOps += 1
                    grid[rowIndex + 1][colIndex] = currentVal
                rowIndex += 1

            rowIndex = 0
            while rowIndex < rowCount:
                if colIndex < colCount - 1 and grid[rowIndex][colIndex] == grid[rowIndex][colIndex + 1]:
                    totalOps += 1
                    candidateValue = 0
                    replaced = False
                    while candidateValue <= 9 and not replaced:
                        if candidateValue != grid[rowIndex][colIndex]:
                            grid[rowIndex][colIndex + 1] = candidateValue
                            replaced = True
                        else:
                            candidateValue += 1
                rowIndex += 1

            colIndex += 1

        return totalOps