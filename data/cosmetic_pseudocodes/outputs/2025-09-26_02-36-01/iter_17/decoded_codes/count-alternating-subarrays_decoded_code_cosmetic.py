class Solution:
    def countAlternatingSubarrays(self, nums):
        size = len(nums)
        if size == 0:
            return 0
        tally = size
        streak = 1
        index = 1
        while index < size:
            if nums[index] != nums[index - 1]:
                streak += 1
            else:
                streak = 1
            tally += streak - 1
            index += 1
        return tally