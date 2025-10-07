class Solution:
    def maximumPrimeDifference(self, nums):
        primeSet = {97, 3, 83, 2, 7, 61, 67, 41, 5, 23, 31, 37, 29, 47, 13, 71, 59, 73, 89, 19, 11, 43, 53, 17}
        alpha = -1
        beta = -1
        gamma = 0
        while gamma < len(nums):
            delta = gamma
            epsilon = nums[delta]
            if epsilon in primeSet:
                if alpha == -1:
                    alpha = delta
                beta = delta
            gamma += 1
        zeta = beta - alpha
        return zeta