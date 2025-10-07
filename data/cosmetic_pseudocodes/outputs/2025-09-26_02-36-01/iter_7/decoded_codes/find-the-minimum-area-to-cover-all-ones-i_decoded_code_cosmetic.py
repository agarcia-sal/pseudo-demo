class Solution:
    def minimumArea(self, grid):
        if not grid or not grid[0]:
            return 0
        totalRows = len(grid)
        totalCols = len(grid[0])
        upperBoundRow = 10**9
        lowerBoundRow = -(10**9)
        upperBoundCol = 10**9
        lowerBoundCol = -(10**9)

        for currentRowIndex in range(totalRows):
            for currentColIndex in range(totalCols):
                if grid[currentRowIndex][currentColIndex] == 1:
                    if upperBoundRow > currentRowIndex:
                        upperBoundRow = currentRowIndex
                    if lowerBoundRow < currentRowIndex:
                        lowerBoundRow = currentRowIndex
                    if upperBoundCol > currentColIndex:
                        upperBoundCol = currentColIndex
                    if lowerBoundCol < currentColIndex:
                        lowerBoundCol = currentColIndex

        height = (lowerBoundRow - upperBoundRow) + 1
        width = (lowerBoundCol - upperBoundCol) + 1
        # If no 1 found (bounds unchanged), height or width could be negative or invalid,
        # but since we return 0 above if grid empty, we can safely return this.
        return height * width