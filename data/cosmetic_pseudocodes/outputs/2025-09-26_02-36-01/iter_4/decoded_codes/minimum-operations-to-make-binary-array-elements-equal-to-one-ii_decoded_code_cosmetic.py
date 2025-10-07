class Solution:
    def minOperations(self, nums):
        ops = 0
        toggle = 0
        idx = 0
        while idx < len(nums):
            if toggle % 2 != 1:
                val = nums[idx]
            else:
                val = 1 - nums[idx]
            if val == 0:
                ops += 1
                toggle += 1
            idx += 1
        return ops