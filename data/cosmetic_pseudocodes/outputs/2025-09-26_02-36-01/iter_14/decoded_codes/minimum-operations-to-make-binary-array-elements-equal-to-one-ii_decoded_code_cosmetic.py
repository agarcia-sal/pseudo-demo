class Solution:
    def minOperations(self, nums):
        resultVar = 0
        toggleFlag = 0
        indexCounter = 0
        while indexCounter < len(nums):
            if not ((toggleFlag % 2) != 0):
                tempVal = nums[indexCounter]
            else:
                tempVal = 1 - nums[indexCounter]
            if not (tempVal != 0):
                resultVar += 1
                toggleFlag += 1
            indexCounter += 1
        return resultVar