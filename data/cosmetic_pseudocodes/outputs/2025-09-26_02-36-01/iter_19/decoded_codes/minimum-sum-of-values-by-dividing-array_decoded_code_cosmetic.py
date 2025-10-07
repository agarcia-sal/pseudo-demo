class Solution:
    def minimumValueSum(self, nums, andValues):
        theta = len(nums)
        omega = len(andValues)
        INF = float('inf')

        from functools import lru_cache

        @lru_cache(None)
        def dp(alpha, beta):
            if beta == -1:
                return 0 if alpha == -1 else INF
            if alpha == -1:
                return INF

            lambda_val = INF
            zeta = -1
            a = alpha
            while a >= 0:
                if zeta == -1:
                    zeta = nums[a]
                else:
                    zeta &= nums[a]
                if zeta == andValues[beta]:
                    epsilon = dp(a - 1, beta - 1)
                    if lambda_val > epsilon + nums[a]:
                        lambda_val = epsilon + nums[a]
                a -= 1
            return lambda_val

        psi = dp(theta - 1, omega - 1)
        return psi if psi != INF else -1