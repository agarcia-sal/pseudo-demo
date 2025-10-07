class Solution:
    def minimumOperations(self, grid):
        totalRows = len(grid)
        totalCols = len(grid[0])
        changesCount = 0
        colIdx = 0

        while colIdx < totalCols:
            rowIdx1 = 0
            # Enforce vertical column consistency
            while rowIdx1 < totalRows - 1:
                if grid[rowIdx1][colIdx] != grid[rowIdx1 + 1][colIdx]:
                    changesCount += 1
                    grid[rowIdx1 + 1][colIdx] = grid[rowIdx1][colIdx]
                rowIdx1 += 1

            rowIdx2 = 0
            # Adjust adjacent columns to avoid same digits vertically
            while rowIdx2 < totalRows:
                nextColExists = colIdx < totalCols - 1
                if nextColExists and grid[rowIdx2][colIdx] == grid[rowIdx2][colIdx + 1]:
                    changesCount += 1
                    digitCandidate = 0
                    while digitCandidate <= 9:
                        if digitCandidate != grid[rowIdx2][colIdx]:
                            grid[rowIdx2][colIdx + 1] = digitCandidate
                            break
                        digitCandidate += 1
                rowIdx2 += 1

            colIdx += 1

        return changesCount