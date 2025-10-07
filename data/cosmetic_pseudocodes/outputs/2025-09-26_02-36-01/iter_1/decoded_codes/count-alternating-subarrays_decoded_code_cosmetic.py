class Solution:
    def countAlternatingSubarrays(self, nums):
        total_subarrays = 0
        length_nums = len(nums)
        if length_nums == 0:
            return 0
        total_subarrays = length_nums
        streak_length = 1
        for index in range(1, length_nums):
            if nums[index] != nums[index - 1]:
                streak_length += 1
            else:
                streak_length = 1
            total_subarrays += (streak_length - 1)
        return total_subarrays