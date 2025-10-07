class Solution:
    def maximumLength(self, nums):
        idx = 1
        len_even = 0
        len_odd = 0
        while idx < len(nums):
            temp_sum = nums[idx - 1] + nums[idx]
            if (temp_sum & 1) == 0:
                len_even = max(len_even + 1, len_odd)
            else:
                len_odd = max(len_odd + 1, len_even)
            idx += 1
        final_res = max(len_even, len_odd) + 1
        return final_res