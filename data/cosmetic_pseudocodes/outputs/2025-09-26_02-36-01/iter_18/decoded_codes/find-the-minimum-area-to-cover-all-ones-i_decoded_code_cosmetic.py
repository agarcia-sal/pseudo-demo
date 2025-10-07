class Solution:
    def minimumArea(self, grid):
        if not grid or not grid[0]:
            return 0

        totalRows = len(grid)
        totalCols = len(grid[0])

        startRow = float('inf')
        endRow = float('-inf')
        startCol = float('inf')
        endCol = float('-inf')

        for outerIndex in range(totalRows):
            for innerIndex in range(totalCols):
                if grid[outerIndex][innerIndex] == 1:
                    if startRow > outerIndex:
                        startRow = outerIndex
                    if endRow < outerIndex:
                        endRow = outerIndex
                    if startCol > innerIndex:
                        startCol = innerIndex
                    if endCol < innerIndex:
                        endCol = innerIndex

        if startRow == float('inf'):
            # no 1 found
            return 0

        calculatedHeight = (endRow - startRow) + 1
        calculatedWidth = (endCol - startCol) + 1
        finalArea = calculatedHeight * calculatedWidth

        return finalArea