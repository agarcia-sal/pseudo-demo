class Solution:
    def maximumTotalCost(self, nums):
        totalCount = len(nums)
        if totalCount == 1:
            return nums[0]

        accumulated = [0] * totalCount
        accumulated[-1] = nums[-1]

        outerIndex = totalCount - 2
        while outerIndex >= 0:
            tempSum = nums[outerIndex]
            if tempSum > accumulated[outerIndex + 1]:
                accumulated[outerIndex] = tempSum
            else:
                accumulated[outerIndex] = tempSum + accumulated[outerIndex + 1]

            innerIndex = outerIndex + 1
            while True:
                signFactor = (-1) ** (innerIndex - outerIndex)
                tempSum += nums[innerIndex] * signFactor

                if innerIndex + 1 < totalCount:
                    candidate = tempSum + accumulated[innerIndex + 1]
                    if accumulated[outerIndex] < candidate:
                        accumulated[outerIndex] = candidate
                else:
                    if accumulated[outerIndex] < tempSum:
                        accumulated[outerIndex] = tempSum

                if innerIndex == totalCount - 1:
                    break
                innerIndex += 1

            outerIndex -= 1

        return accumulated[0]