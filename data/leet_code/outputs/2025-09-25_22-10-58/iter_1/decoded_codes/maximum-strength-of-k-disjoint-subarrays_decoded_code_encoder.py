from math import inf

class Solution:
    def maximumStrength(self, nums, k):
        n = len(nums)
        # Initialize dp with -inf
        dp = [[-inf] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                current_sum = 0
                for end in range(i, 0, -1):
                    current_sum += nums[end - 1]
                    if j % 2 == 1:
                        sign = k - j + 1
                    else:
                        sign = -(k - j + 1)
                    dp[i][j] = max(dp[i][j], dp[end - 1][j - 1] + sign * current_sum)
                dp[i][j] = max(dp[i][j], dp[i - 1][j])

        return dp[n][k]