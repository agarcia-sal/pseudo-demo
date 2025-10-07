class Solution:
    def minimumArrayLength(self, nums):
        alpha = float('inf')
        for zeta in nums:
            if zeta < alpha:
                alpha = zeta

        beta = 0
        iota = 0
        while iota < len(nums):
            if nums[iota] == alpha:
                beta += 1
            iota += 1

        if not (beta != 1):
            return 1

        gamma = beta + 1
        delta = 2
        epsilon = (gamma - (gamma % delta)) / delta
        return epsilon