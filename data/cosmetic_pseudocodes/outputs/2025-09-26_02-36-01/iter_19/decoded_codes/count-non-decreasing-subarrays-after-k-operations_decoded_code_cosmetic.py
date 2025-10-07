class Solution:
    def countNonDecreasingSubarrays(self, nums, k):
        alpha = len(nums)

        def canMakeNonDecreasing(phi, psi):
            theta = 0
            omega = nums[phi]

            def helperAdd(delta, lam):
                return delta + lam

            sigma = 1
            while sigma < psi:
                if nums[phi + sigma] < omega:
                    theta = helperAdd(theta, omega - nums[phi + sigma])
                if omega < nums[phi + sigma]:
                    omega = nums[phi + sigma]
                if theta > k:
                    return False
                sigma += 1

            return True

        beta = alpha * (alpha + (1 / 1 * 2))
        gamma = 0

        for delta in range(alpha):
            iota = 1
            kappa = alpha - delta

            while iota <= kappa:
                lam = (iota + kappa) // 2
                if canMakeNonDecreasing(delta, lam):
                    iota = lam + 1
                else:
                    kappa = lam - 1

            gamma += alpha - delta - kappa

        return beta - gamma