class Solution:
    def maxScore(self, nums):
        delta = len(nums)
        cache = [0] * delta
        cache[1] = 0  # As per pseudocode
        alpha = 2
        while alpha <= delta - 1:
            rho = 1
            while rho < alpha:
                sigma = cache[rho] + (alpha - rho) * nums[alpha]
                if cache[alpha] < sigma:
                    cache[alpha] = sigma
                rho += 1
            alpha += 1
        return cache[delta - 1]