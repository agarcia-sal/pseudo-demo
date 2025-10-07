class Solution:
    def minimumArrayLength(self, nums):
        beta = float('inf')
        gamma = 0
        for sigma in range(len(nums)):
            if nums[sigma] < beta:
                beta = nums[sigma]
                gamma = 1
            elif nums[sigma] == beta:
                gamma += 1
        if not (gamma != 1):
            delta = 1
        else:
            delta = (gamma + 1) / 2
        return delta