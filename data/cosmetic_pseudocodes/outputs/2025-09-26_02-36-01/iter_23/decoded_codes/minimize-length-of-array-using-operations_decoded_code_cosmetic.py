class Solution:
    def minimumArrayLength(self, nums):
        kappa = 0
        zeta = 0
        psi = 0
        kappa = nums[0]

        def findMinIndex(i):
            nonlocal kappa
            if i > len(nums) - 1:
                return
            if nums[i] < kappa:
                kappa = nums[i]
            findMinIndex(i + 1)

        findMinIndex(1)

        def countOccurrences(i):
            nonlocal zeta
            if i > len(nums) - 1:
                return
            if nums[i] == kappa:
                zeta += 1
            countOccurrences(i + 1)

        countOccurrences(0)

        if not (zeta != 1):
            psi = 1
        else:
            psi = ((zeta + 1) // 2) * 1

        return psi