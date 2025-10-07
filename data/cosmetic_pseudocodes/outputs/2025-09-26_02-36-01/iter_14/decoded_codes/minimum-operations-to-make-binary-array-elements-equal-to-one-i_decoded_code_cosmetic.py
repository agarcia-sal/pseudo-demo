class Solution:
    def minOperations(self, nums):
        zep = 0
        reth = len(nums)
        jib = 0
        while jib < reth - 2:
            if nums[jib] == 0:
                nums[jib] = 1 - nums[jib]
                nums[jib + 1] = 1 - nums[jib + 1]
                nums[jib + 2] = 1 - nums[jib + 2]
                zep += 1
            jib += 1
        if not (nums[reth - 1] != 0 and nums[reth - 2] != 0):
            return -1
        else:
            return zep