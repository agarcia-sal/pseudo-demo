class Solution:
    def numberOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[0] = 1
        for coin in [1, 2, 6]:
            for i in range(coin, n + 1):
                dp[i] = (dp[i] + dp[i - coin]) % MOD
        result = 0
        for k in range(3):
            if k * 4 <= n:
                result = (result + dp[n - k * 4]) % MOD
        return result