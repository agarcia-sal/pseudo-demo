class Solution:
    def maximumLength(self, nums):
        alpha = 0
        beta = 0
        gamma = 1
        while gamma < len(nums):
            delta = nums[gamma - 1] + nums[gamma]
            if delta % 2 == 0:
                alpha = max(alpha + 1, beta)
            else:
                beta = max(beta + 1, alpha)
            gamma += 1
        epsilon = max(alpha, beta) + 1
        return epsilon