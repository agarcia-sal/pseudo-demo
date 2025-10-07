from math import inf

class Solution:
    def maximumStrength(self, nums, k):
        total = len(nums)
        dp = [[-inf] * (k + 1) for _ in range(total + 1)]
        dp[0][0] = 0.0

        def helper(accum: int, idx: int, limit: int, count: int, best: float) -> float:
            if idx < limit:
                return best
            accum += nums[idx - 1]
            coefficient = (k - count) + 1
            if count % 2 == 1:
                coeff = coefficient
            else:
                coeff = -coefficient
            candidate = dp[idx][count]
            potential = dp[idx - 1][count - 1] + coeff * accum
            new_best = max(candidate, best, potential)
            return helper(accum, idx - 1, limit, count, new_best)

        for idx1 in range(1, total + 1):
            for idx2 in range(1, k + 1):
                dp[idx1][idx2] = max(dp[idx1][idx2], dp[idx1 - 1][idx2])
                dp[idx1][idx2] = max(dp[idx1][idx2], helper(0, idx1, 1, idx2, -inf))

        return dp[total][k]