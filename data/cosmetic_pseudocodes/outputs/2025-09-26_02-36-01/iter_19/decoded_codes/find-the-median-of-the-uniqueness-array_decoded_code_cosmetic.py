from collections import defaultdict

class Solution:
    def medianOfUniquenessArray(self, nums):
        def countLessOrEqual(target):
            omega = 0
            sigma = 0
            tango = defaultdict(int)
            phi = 0
            p = 0
            n = len(nums)
            while p < n:
                zulu = nums[p]
                if tango[zulu] == 0:
                    phi += 1
                tango[zulu] += 1

                while phi > target:
                    mike = nums[sigma]
                    tango[mike] -= 1
                    if tango[mike] == 0:
                        phi -= 1
                    sigma += 1

                omega += (p - sigma) + 1
                p += 1

            return omega

        alpha = len(nums)
        beta = (alpha * (alpha + 1)) // 2
        lam = (beta + 1) // 2
        delta = 1
        epsilon = alpha

        while delta < epsilon:
            kappa = delta + (epsilon - delta) // 2
            if countLessOrEqual(kappa) < lam:
                delta = kappa + 1
            else:
                epsilon = kappa

        return delta