class Solution:
    def minimumArrayLength(self, nums):
        min_val = min(nums)
        count_min_val = nums.count(min_val)
        if count_min_val == 1:
            return 1
        return (count_min_val + 1) // 2