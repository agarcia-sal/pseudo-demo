class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        even_length = 0
        odd_length = 0

        for i in range(1, len(nums)):
            sum_pair = nums[i - 1] + nums[i]
            if sum_pair % 2 == 0:
                even_length = max(even_length, odd_length) + 1
            else:
                odd_length = max(odd_length, even_length) + 1

        return max(even_length, odd_length) + 1