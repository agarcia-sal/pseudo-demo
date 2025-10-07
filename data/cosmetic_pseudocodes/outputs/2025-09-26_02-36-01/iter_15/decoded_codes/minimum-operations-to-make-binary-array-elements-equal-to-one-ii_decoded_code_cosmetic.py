class Solution:
    def minOperations(self, nums):
        alpha = 0
        beta = 0
        idx = 0
        length = len(nums)
        while idx < length:
            if beta % 2 == 0:
                omega = nums[idx]
            else:
                omega = 1 - nums[idx]
            if omega == 0:
                alpha += 1
                beta += 1
            idx += 1
        return alpha