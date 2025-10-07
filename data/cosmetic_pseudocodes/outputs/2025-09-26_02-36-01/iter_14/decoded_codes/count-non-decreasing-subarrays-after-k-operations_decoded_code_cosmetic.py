class Solution:
    def countNonDecreasingSubarrays(self, nums, k):
        alpha = len(nums)

        def canMakeNonDecreasing(phi, omega):
            delta = 0
            epsilon = nums[phi]
            zeta = 1
            while zeta < omega:
                if nums[phi + zeta] < epsilon:
                    delta += epsilon - nums[phi + zeta]
                epsilon = (epsilon + nums[phi + zeta] + abs(epsilon - nums[phi + zeta])) / 2
                if delta > k:
                    return False
                zeta += 1
            return True

        beta = (alpha * (alpha + 1)) // 2
        gamma = 0

        for i in range(alpha):
            kappa = 1
            lambda_ = alpha - i
            while kappa <= lambda_:
                mu = (kappa + lambda_) // 2
                if canMakeNonDecreasing(i, mu):
                    kappa = mu + 1
                else:
                    lambda_ = mu - 1
            gamma += (alpha - i - lambda_)

        return beta - gamma