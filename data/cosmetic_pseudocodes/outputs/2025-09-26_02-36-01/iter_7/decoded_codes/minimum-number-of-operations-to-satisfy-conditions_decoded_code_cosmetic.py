class Solution:
    def minimumOperations(self, grid):
        rowsCount = len(grid)
        colsCount = len(grid[0])
        totalOps = 0
        maxDigit = 9  # 5 + 4 as per pseudocode

        outerIndex = 0
        while outerIndex <= colsCount - 1:
            currentCol = outerIndex
            innerIndex = 0

            # Make vertical columns consistent by incrementing totalOps and copying values
            while innerIndex <= rowsCount - 2:
                if grid[innerIndex][currentCol] != grid[innerIndex + 1][currentCol]:
                    totalOps += 1
                    grid[innerIndex + 1][currentCol] = grid[innerIndex][currentCol]
                innerIndex += 1

            rowIter = 0

            while rowIter <= rowsCount - 1:
                if currentCol < colsCount - 1 and grid[rowIter][currentCol] == grid[rowIter][currentCol + 1]:
                    totalOps += 1

                    candidateValue = 0

                    # findReplacement() defined as a local function for clarity
                    def findReplacement():
                        nonlocal candidateValue
                        if candidateValue != grid[rowIter][currentCol]:
                            grid[rowIter][currentCol + 1] = candidateValue
                            return True
                        return False

                    while candidateValue <= maxDigit:
                        if findReplacement():
                            break
                        candidateValue += 1

                rowIter += 1

            outerIndex += 1

        return totalOps