class Solution:
    def maximumLength(self, nums):
        alpha = 0
        beta = 0
        delta = 1

        while delta < len(nums):
            epsilon = nums[delta - 1] + nums[delta]
            zeta = epsilon % 2
            if zeta == 0:
                alpha = max(alpha + 1, beta)
            else:
                beta = max(beta + 1, alpha)

            delta += 1

        eta = max(alpha, beta) + 1
        return eta