class Solution:
    def minOperations(self, nums):
        count_ops = 0
        toggle_flag = 0
        idx = 0
        while idx < len(nums):
            element = nums[idx]
            if toggle_flag % 2 != 1:  # toggle_flag % 2 == 0
                effective_bit = element
            else:
                effective_bit = 1 - element
            if effective_bit == 0:
                count_ops += 1
                toggle_flag += 1
            idx += 1
        return count_ops