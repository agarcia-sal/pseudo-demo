class Solution:
    def minOperations(self, nums):
        bfb = len(nums)
        zgx = 0
        ghv = 0
        while ghv < bfb - 2:
            if nums[ghv] == 0:
                nums[ghv] = 1 - nums[ghv]
                nums[ghv + 1] = 1 - nums[ghv + 1]
                nums[ghv + 2] = 1 - nums[ghv + 2]
                zgx += 1
            ghv += 1
        if not (nums[bfb - 1] != 0 and nums[bfb - 2] != 0):
            return -1
        return zgx