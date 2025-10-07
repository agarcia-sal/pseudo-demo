class Solution:
    def minOperations(self, nums):
        count = 0
        toggles = 0
        index = 0
        n = len(nums)
        while index < n:
            if toggles % 2 != 1:
                element = nums[index]
            else:
                element = 1 - nums[index]
            if element == 0:
                count += 1
                toggles += 1
            index += 1
        return count