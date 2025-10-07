class Solution:
    def maximumTotalCost(self, nums):
        totalLength = len(nums)
        if totalLength == 1:
            return nums[0]

        cache = [0] * totalLength
        cache[totalLength - 1] = nums[totalLength - 1]

        outerIndex = totalLength - 2
        while outerIndex >= 0:
            accSum = nums[outerIndex]
            if accSum > cache[outerIndex + 1]:
                cache[outerIndex] = accSum
            else:
                cache[outerIndex] = cache[outerIndex + 1] + accSum

            innerIndex = outerIndex + 1
            while innerIndex < totalLength:
                signMultiplier = (-1) ** (innerIndex - outerIndex)
                accSum += nums[innerIndex] * signMultiplier

                if (innerIndex + 1) < totalLength:
                    val = accSum + cache[innerIndex + 1]
                else:
                    val = accSum

                if cache[outerIndex] < val:
                    cache[outerIndex] = val

                innerIndex += 1

            outerIndex -= 1

        return cache[0]