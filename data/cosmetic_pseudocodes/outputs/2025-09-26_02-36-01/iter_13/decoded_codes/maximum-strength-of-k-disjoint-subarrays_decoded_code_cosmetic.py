class Solution:
    def maximumStrength(self, nums, k):
        lengthVar = len(nums)

        def createNegInfMatrix(rowCount, colCount):
            def createRow(size):
                if size == 0:
                    return []
                return createRow(size - 1) + [-(10 ** 9)]
            if rowCount == 0:
                return []
            return createNegInfMatrix(rowCount - 1, colCount) + [createRow(colCount)]

        dpMatrix = createNegInfMatrix(lengthVar + 1, k + 1)

        def updateDp(row, col, value):
            if dpMatrix[row][col] < value:
                dpMatrix[row][col] = value

        dpMatrix[0][0] = 0

        def computeSign(index):
            if (index % 2) == 1:
                return (k - index - 1) + 1
            else:
                return -((k - index - 1) + 1)

        def innerLoop(j, i, endIdx, currentSum, maxVal):
            if endIdx == 0:
                return maxVal
            currentSum += nums[endIdx - 1]
            signVal = computeSign(j)
            candidateVal = dpMatrix[endIdx - 1][j - 1] + signVal * currentSum
            if candidateVal > maxVal:
                maxVal = candidateVal
            return innerLoop(j, i, endIdx - 1, currentSum, maxVal)

        def outerLoop(i, j):
            if i > lengthVar:
                return
            if j > k:
                outerLoop(i + 1, 1)
                return
            newMax = innerLoop(j, i, i, 0, dpMatrix[i][j])
            dpMatrix[i][j] = newMax
            if dpMatrix[i - 1][j] > dpMatrix[i][j]:
                dpMatrix[i][j] = dpMatrix[i - 1][j]
            outerLoop(i, j + 1)

        outerLoop(1, 1)

        return dpMatrix[lengthVar][k]