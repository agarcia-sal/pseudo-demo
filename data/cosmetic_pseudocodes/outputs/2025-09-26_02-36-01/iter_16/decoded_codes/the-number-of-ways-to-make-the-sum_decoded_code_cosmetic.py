class Solution:
    def numberOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[0] = 1
        coins = [6, 1, 2]

        for c in coins:
            for i in range(c, n + 1):
                dp[i] = (dp[i] + dp[i - c]) % MOD

        result = 0
        for k in range(3):
            offset = k * 4
            if offset <= n:
                result = (result + dp[n - offset]) % MOD

        return result