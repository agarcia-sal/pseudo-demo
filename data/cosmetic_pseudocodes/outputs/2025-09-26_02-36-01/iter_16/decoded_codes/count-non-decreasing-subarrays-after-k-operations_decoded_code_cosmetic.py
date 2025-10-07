class Solution:
    def countNonDecreasingSubarrays(self, nums, k):
        n = len(nums)

        def canMakeNonDecreasing(alpha, beta):
            delta = 0
            omega = nums[alpha]
            idx = 1
            while idx < beta:
                if nums[alpha + idx] < omega:
                    delta += omega - nums[alpha + idx]
                if omega < nums[alpha + idx]:
                    omega = nums[alpha + idx]
                if delta > k:
                    return False
                idx += 1
            return True

        sigma = n * (n + 1) // 2
        phi = 0

        zeta = 0
        while zeta < n:
            epsilon = 1
            gamma = n - zeta
            while epsilon <= gamma:
                tau = (epsilon + gamma) // 2
                if canMakeNonDecreasing(zeta, tau):
                    epsilon = tau + 1
                else:
                    gamma = tau - 1
            phi += n - zeta - gamma
            zeta += 1

        return sigma - phi