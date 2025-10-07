class Solution:
    def minimumOperations(self, nums, target):
        lengthOfNums = len(nums)
        initialDiff = abs(target[0] - nums[0])
        totalOps = initialDiff
        index = 1
        while index < lengthOfNums:
            currentDiff = target[index] - nums[index]
            previousDiff = target[index - 1] - nums[index - 1]
            if currentDiff * previousDiff > 0:
                delta = abs(abs(currentDiff) - abs(previousDiff))
                if delta > 0:
                    totalOps += delta
            else:
                totalOps += abs(currentDiff)
            index += 1
        return totalOps