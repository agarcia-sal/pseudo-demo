from collections import defaultdict
from math import floor

class Solution:
    def medianOfUniquenessArray(self, nums):
        def countLessOrEqual(target):
            alpha = 0
            beta = 0
            gamma = defaultdict(int)
            delta = 0
            zeta = 0
            n = len(nums)
            while zeta < n:
                if gamma[nums[zeta]] == 0:
                    delta += 1
                gamma[nums[zeta]] += 1
                while delta > target:
                    gamma[nums[beta]] -= 1
                    if gamma[nums[beta]] == 0:
                        delta -= 1
                    beta += 1
                alpha += zeta - beta + 1
                zeta += 1
            return alpha

        n = len(nums)
        epsilon = n * (n + 1) // 2
        eta = (epsilon + 1) // 2
        theta = 1
        iota = n

        while theta < iota:
            kappa = (theta + iota) // 2
            if countLessOrEqual(kappa) < eta:
                theta = kappa + 1
            else:
                iota = kappa

        return theta