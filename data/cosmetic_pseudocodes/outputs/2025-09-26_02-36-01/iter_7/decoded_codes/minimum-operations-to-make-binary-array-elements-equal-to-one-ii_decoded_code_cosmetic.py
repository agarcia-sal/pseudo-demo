from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        op_count = 0
        toggle_flag = 0
        idx = 0
        length = len(nums)
        while idx < length:
            if (toggle_flag % 2) == 0:
                val = nums[idx]
            else:
                val = 1 - nums[idx]
            if val == 0:
                op_count += 1
                toggle_flag += 1
            idx += 1
        return op_count