class Solution:
    def maximumLength(self, nums):
        count_even = 0
        count_odd = 0
        index = 1
        while index < len(nums):
            pair_sum = nums[index - 1] + nums[index]
            if (pair_sum & 1) == 0:
                count_even = max(count_even + 1, count_odd)
            else:
                count_odd = max(count_odd + 1, count_even)
            index += 1
        maximum_length = max(count_even, count_odd) + 1
        return maximum_length