class Solution:
    def countAlternatingSubarrays(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        count = n
        current_length = 1
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                current_length += 1
            else:
                current_length = 1
            count += current_length - 1
        return count