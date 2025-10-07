class Solution:
    def minOperations(self, nums):
        tally = 0
        toggle_marker = 0
        idx = 0
        n = len(nums)
        while idx < n:
            if toggle_marker % 2 == 0:
                temp_val = nums[idx]
            else:
                temp_val = 1 - nums[idx]

            if temp_val == 0:
                tally += 1
                toggle_marker += 1
            idx += 1
        return tally