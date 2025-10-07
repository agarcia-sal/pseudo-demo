class Solution:
    def maximumStrength(self, nums, k):
        n = len(nums)
        # Initialize DP array with very small numbers
        dp = [[-1 << 30] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        def process_segment(x, i, j):
            if j < 1:
                return
            else:
                cum_sum = 0
                for idx in range(j, x - 1, -1):
                    cum_sum += nums[idx - 1]
                    if j % 2 == 1:
                        multiplier = k - j
                    else:
                        multiplier = -(k - j)
                    dp[j][j] = max(dp[j][j], dp[idx - 1][j - 1] + multiplier * cum_sum)
                dp[j][j] = max(dp[j][j], dp[j - 1][j])

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                process_segment(1, i, j)

        return dp[n][k]