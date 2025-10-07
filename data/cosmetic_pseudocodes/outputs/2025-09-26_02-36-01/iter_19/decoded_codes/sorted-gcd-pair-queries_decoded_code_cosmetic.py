from collections import Counter
from math import ceil, floor

class Solution:
    def gcdValues(self, nums, queries):
        upperLimit = nums[0]
        for index in range(1, len(nums)):
            if nums[index] > upperLimit:
                upperLimit = nums[index]

        tally = Counter()
        for item in nums:
            tally[item] += 1

        aggregates = [0] * (upperLimit + 1)

        for current in range(upperLimit, 0, -1):
            tempCount = 0
            step = current
            while step <= upperLimit:
                tempCount += tally.get(step, 0)
                aggregates[current] -= aggregates[step]
                step += current
            aggregates[current] += tempCount * (tempCount - 1) // 2

        for idx in range(1, len(aggregates)):
            aggregates[idx] += aggregates[idx - 1]

        def binarySearchRightBound(array, target):
            lowBound, highBound = 0, len(array)
            while lowBound < highBound:
                midPoint = (lowBound + highBound) / 2
                if target < array[floor(midPoint)]:
                    highBound = floor(midPoint)
                else:
                    lowBound = ceil(midPoint + 1)
            return lowBound

        output = []
        for item in queries:
            output.append(binarySearchRightBound(aggregates, item))

        return output