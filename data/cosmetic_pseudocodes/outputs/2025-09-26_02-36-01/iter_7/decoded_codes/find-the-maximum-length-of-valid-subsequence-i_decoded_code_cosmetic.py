class Solution:
    def maximumLength(self, nums):
        len_even = 0
        len_odd = 0

        for idx in range(1, len(nums)):
            temp_sum = nums[idx - 1] + nums[idx]
            if temp_sum % 2 == 0:
                len_even = max(len_even + 1, len_odd)
            else:
                len_odd = max(len_odd + 1, len_even)

        return max(len_even, len_odd) + 1