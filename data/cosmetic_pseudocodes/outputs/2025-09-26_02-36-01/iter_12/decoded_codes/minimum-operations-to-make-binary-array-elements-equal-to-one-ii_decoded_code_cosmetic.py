class Solution:
    def minOperations(self, nums):
        opCount = 0
        toggleFlag = 0

        def checkParity(value):
            return value % 2 == 0

        index = 0
        length = len(nums)
        while index < length:
            parityStatus = checkParity(toggleFlag)
            currentElement = nums[index] if parityStatus else 1 - nums[index]

            if currentElement == 0:
                opCount += 1
                toggleFlag += 1
            index += 1

        return opCount