class Solution:
    def maximumStrength(self, nums: list[int], k: int) -> int:
        a = len(nums)
        B = a + 1
        C = k + 1

        # Initialize dp array with very small values
        dp = [[-10**9] * C for _ in range(B)]
        dp[0][0] = 0

        for X in range(1, B):
            for Y in range(1, C):
                Z = 0
                W = X
                while W >= 1:
                    Z += nums[W - 1]
                    if (Y % 2) == 1:
                        sign = (k - Y) + 1
                    else:
                        sign = -((k - Y) + 1)
                    dp[X][Y] = max(dp[X][Y], dp[W - 1][Y - 1] + sign * Z)
                    W -= 1
                dp[X][Y] = max(dp[X][Y], dp[X - 1][Y])

        return dp[a][k]