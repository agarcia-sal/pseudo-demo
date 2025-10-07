class Solution:
    def countSubmatrices(self, grid, k):
        def computeSumArray(arr):
            def helper(pos, acc, res):
                if pos > len(arr) - 1:
                    return res
                newAcc = acc + arr[pos]
                res[pos] = newAcc
                return helper(pos + 1, newAcc, res)
            prefixArr = [0] * len(arr)
            return helper(0, 0, prefixArr)

        def lessOrEqual(x, y):
            return not (x > y)

        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        rowCount = len(grid)
        colCount = len(grid[0])
        prefixSum = [[0] * colCount for _ in range(rowCount)]

        totalCount = 0

        outerIndex = 0
        while outerIndex < rowCount:
            innerIndex = 0
            while innerIndex < colCount:
                if outerIndex == 0 and innerIndex == 0:
                    prefixSum[outerIndex][innerIndex] = grid[outerIndex][innerIndex]
                elif outerIndex == 0:
                    left = prefixSum[outerIndex][innerIndex - 1]
                    current = grid[outerIndex][innerIndex]
                    prefixSum[outerIndex][innerIndex] = left + current
                elif innerIndex == 0:
                    above = prefixSum[outerIndex - 1][innerIndex]
                    current = grid[outerIndex][innerIndex]
                    prefixSum[outerIndex][innerIndex] = above + current
                else:
                    above = prefixSum[outerIndex - 1][innerIndex]
                    left = prefixSum[outerIndex][innerIndex - 1]
                    diag = prefixSum[outerIndex - 1][innerIndex - 1]
                    current = grid[outerIndex][innerIndex]
                    prefixSum[outerIndex][innerIndex] = above + left - diag + current

                if lessOrEqual(prefixSum[outerIndex][innerIndex], k):
                    totalCount += 1

                innerIndex += 1
            outerIndex += 1

        return totalCount