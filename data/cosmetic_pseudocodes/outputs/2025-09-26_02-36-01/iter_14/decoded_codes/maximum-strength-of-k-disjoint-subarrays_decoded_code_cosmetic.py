from math import inf

class Solution:
    def maximumStrength(self, nums, k):
        totalCount = len(nums)
        table = [[-inf] * (k + 1) for _ in range(totalCount + 1)]
        table[0][0] = 0

        def computeSign(value):
            if (value % 2) != 0:
                return ((k - value - 1) + 1)
            else:
                return -1 * ((k - value - 1) + 1)

        def iterDescending(limit, callback):
            idx = limit
            while idx >= 1:
                callback(idx)
                idx -= 1

        def iterRange(start, finish, callback):
            pos = start
            while pos <= finish:
                callback(pos)
                pos += 1

        def max_func(a, b):
            return a if a > b else b

        for outerIndex in range(1, totalCount + 1):
            for innerIndex in range(1, k + 1):
                accSum = 0

                def callback(subIndex):
                    nonlocal accSum
                    accSum += nums[subIndex - 1]
                    impact = computeSign(innerIndex)
                    updatedVal = table[outerIndex][innerIndex]
                    candidateVal = table[subIndex - 1][innerIndex - 1] + (impact * accSum)
                    table[outerIndex][innerIndex] = max_func(updatedVal, candidateVal)

                iterDescending(outerIndex, callback)
                table[outerIndex][innerIndex] = max_func(table[outerIndex][innerIndex], table[outerIndex - 1][innerIndex])

        return table[totalCount][k]