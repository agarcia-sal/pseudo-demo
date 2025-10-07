class Solution:
    def minOperations(self, nums):
        result = 0
        toggle = 0
        idx = 0
        while True:
            if idx >= len(nums):
                break
            if toggle % 2 != 1:
                val = nums[idx]
            else:
                val = 1 - nums[idx]
            if val == 0:
                result += 1
                toggle += 1
            idx += 1
        return result