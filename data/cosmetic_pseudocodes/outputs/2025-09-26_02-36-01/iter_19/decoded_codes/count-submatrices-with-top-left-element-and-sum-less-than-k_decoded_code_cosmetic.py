class Solution:
    def countSubmatrices(self, grid, k):
        if not grid or not grid[0]:
            return 0

        rowsCount, colsCount = len(grid), len(grid[0])
        sums = [[0] * colsCount for _ in range(rowsCount)]
        retVal = 0

        for outerIndex in range(rowsCount):
            for innerIndex in range(colsCount):
                if outerIndex == 0:
                    if innerIndex == 0:
                        sums[outerIndex][innerIndex] = grid[outerIndex][innerIndex]
                    else:
                        sums[outerIndex][innerIndex] = sums[outerIndex][innerIndex - 1] + grid[outerIndex][innerIndex]
                else:
                    if innerIndex == 0:
                        sums[outerIndex][innerIndex] = sums[outerIndex - 1][innerIndex] + grid[outerIndex][innerIndex]
                    else:
                        sums[outerIndex][innerIndex] = (
                            sums[outerIndex][innerIndex - 1]
                            + sums[outerIndex - 1][innerIndex]
                            - sums[outerIndex - 1][innerIndex - 1]
                            + grid[outerIndex][innerIndex]
                        )
                if sums[outerIndex][innerIndex] <= k:
                    retVal += 1

        return retVal