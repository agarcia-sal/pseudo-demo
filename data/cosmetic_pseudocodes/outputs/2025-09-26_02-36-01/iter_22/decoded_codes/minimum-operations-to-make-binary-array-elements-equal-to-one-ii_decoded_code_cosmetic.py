from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        idx = 0
        total_ops = 0
        toggle_flag = 0
        n = len(nums)
        while idx < n:
            if (toggle_flag % 2) == 0:
                temp_val = nums[idx]
            else:
                temp_val = 1 - nums[idx]
            if temp_val == 0:
                total_ops += 1
                toggle_flag += 1
            idx += 1
        return total_ops