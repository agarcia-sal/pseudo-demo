class Solution:
    def minOperations(self, nums):
        lengthCount = len(nums)
        opsCounter = 0
        indexIter = 0
        # Iterate until lengthCount - 2 (since we access indexIter+2 inside loop)
        while indexIter < lengthCount - 2:
            currentVal = nums[indexIter]
            if currentVal == 0:
                nums[indexIter] = 1 - nums[indexIter]
                nextIndex = indexIter + 1
                nums[nextIndex] = 1 - nums[nextIndex]
                nextNextIndex = indexIter + 2
                nums[nextNextIndex] = 1 - nums[nextNextIndex]
                opsCounter += 1
            indexIter += 1
        lastIndex = lengthCount - 1
        secondLastIndex = lengthCount - 2
        if nums[lastIndex] == 0 or nums[secondLastIndex] == 0:
            return -1
        return opsCounter