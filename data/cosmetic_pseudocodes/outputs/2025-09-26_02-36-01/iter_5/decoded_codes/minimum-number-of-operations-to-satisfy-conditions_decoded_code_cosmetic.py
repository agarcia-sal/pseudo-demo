class Solution:
    def minimumOperations(self, grid):
        rowCount = len(grid)
        colCount = len(grid[0])
        totalOps = 0

        def compareAndFix(current, next_row, col):
            nonlocal totalOps
            if current[col] != next_row[col]:
                totalOps += 1
                next_row[col] = current[col]

        def alterNextValue(row, col):
            nonlocal totalOps
            if col < colCount - 1 and grid[row][col] == grid[row][col + 1]:
                totalOps += 1
                replacementFound = False
                candidateValue = 0
                while not replacementFound and candidateValue <= 9:
                    if candidateValue != grid[row][col]:
                        grid[row][col + 1] = candidateValue
                        replacementFound = True
                    candidateValue += 1

        currentCol = 0
        while currentCol <= colCount - 1:
            currentRow = 0
            while currentRow <= rowCount - 2:
                compareAndFix(grid[currentRow], grid[currentRow + 1], currentCol)
                currentRow += 1

            currentRow = 0
            while currentRow <= rowCount - 1:
                alterNextValue(currentRow, currentCol)
                currentRow += 1

            currentCol += 1

        result = totalOps
        return result