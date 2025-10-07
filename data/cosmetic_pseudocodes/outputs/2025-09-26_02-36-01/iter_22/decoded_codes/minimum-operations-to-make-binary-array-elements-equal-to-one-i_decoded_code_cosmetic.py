class Solution:
    def minOperations(self, nums):
        n = len(nums)
        count = 0
        i = 0
        while i < n - 2:
            if nums[i] == 0:
                nums[i] = 1 - nums[i]
                nums[i + 1] = 1 - nums[i + 1]
                nums[i + 2] = 1 - nums[i + 2]
                count += 1
            i += 1
        if nums[-1] == 0 or nums[-2] == 0:
            return -1
        return count