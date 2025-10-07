class Solution:
    def maximumLength(self, nums):
        even_length = 0
        odd_length = 0
        for i in range(1, len(nums)):
            current_sum = nums[i - 1] + nums[i]
            if current_sum % 2 == 0:
                even_length = max(even_length + 1, odd_length)
            else:
                odd_length = max(odd_length + 1, even_length)
        return max(even_length, odd_length) + 1