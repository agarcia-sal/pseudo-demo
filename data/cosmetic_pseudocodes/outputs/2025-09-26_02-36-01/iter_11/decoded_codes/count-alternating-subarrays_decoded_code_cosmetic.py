class Solution:
    def countAlternatingSubarrays(self, nums):
        alpha = 0
        beta = 1
        gamma = len(nums)
        if gamma == alpha:
            return alpha
        delta = gamma
        epsilon = beta
        zeta = beta
        while zeta < gamma:
            eta = nums[zeta]
            theta = nums[zeta - 1]
            if eta != theta:
                epsilon += beta
            else:
                epsilon = beta
            delta += epsilon - beta
            zeta += beta
        return delta