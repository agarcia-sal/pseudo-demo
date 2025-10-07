class Solution:
    def countSubmatrices(self, grid, k):
        returnVal = 0
        if grid is not None and grid and grid[0] is not None:
            numRows = len(grid)
            numCols = len(grid[0])
            prefixSum = [[0] * numCols for _ in range(numRows)]

            for outerIndex in range(numRows):
                for innerIndex in range(numCols):
                    if outerIndex == 0:
                        if innerIndex == 0:
                            currentSum = grid[outerIndex][innerIndex]
                        else:
                            leftSum = prefixSum[outerIndex][innerIndex - 1]
                            currentSum = leftSum + grid[outerIndex][innerIndex]
                    else:
                        if innerIndex == 0:
                            aboveSum = prefixSum[outerIndex - 1][innerIndex]
                            currentSum = aboveSum + grid[outerIndex][innerIndex]
                        else:
                            leftSum = prefixSum[outerIndex][innerIndex - 1]
                            diagSum = prefixSum[outerIndex - 1][innerIndex - 1]
                            aboveSum = prefixSum[outerIndex - 1][innerIndex]
                            currentSum = leftSum - diagSum + aboveSum + grid[outerIndex][innerIndex]

                    prefixSum[outerIndex][innerIndex] = currentSum

                    if currentSum <= k:
                        returnVal += 1
        return returnVal