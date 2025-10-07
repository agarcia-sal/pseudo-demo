class Solution:
    def minOperations(self, nums):
        totalCount = len(nums)
        opCount = 0
        index = 0

        while index < totalCount - 2:
            if nums[index] == 0:
                nums[index] = 1 - nums[index]
                nums[index + 1] = 1 - nums[index + 1]
                nums[index + 2] = 1 - nums[index + 2]
                opCount += 1
            index += 1

        if nums[totalCount - 1] == 0 or nums[totalCount - 2] == 0:
            return -1
        return opCount