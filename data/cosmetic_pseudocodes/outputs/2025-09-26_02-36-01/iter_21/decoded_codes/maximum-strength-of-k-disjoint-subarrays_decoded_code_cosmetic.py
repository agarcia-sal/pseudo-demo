class Solution:
    def maximumStrength(self, nums, k: int) -> int:
        n = len(nums)
        # Initialize dp with very small values (-1 << 20) to simulate -inf
        dp = [[-1 << 20] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for m in range(1, n + 1):
            for j in range(1, k + 1):
                prefix_sum = 0
                r = m
                while r >= 1:
                    prefix_sum += nums[r - 1]
                    # Using the original check of parity for j
                    if j % 2 == 1:
                        s = -(k - j + 1)
                    else:
                        s = k - j + 1

                    without_current = dp[m][j]
                    with_current = dp[r - 1][j - 1] + s * prefix_sum

                    if with_current > without_current:
                        dp[m][j] = with_current

                    r -= 1

                if dp[m][j] < dp[m - 1][j]:
                    dp[m][j] = dp[m - 1][j]

        return dp[n][k]