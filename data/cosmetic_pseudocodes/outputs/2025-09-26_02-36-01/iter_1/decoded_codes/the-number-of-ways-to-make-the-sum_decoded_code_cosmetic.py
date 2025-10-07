class Solution:
    def numberOfWays(self, n: int) -> int:
        MODULO = 10**9 + 7
        dp = [0] * (n + 1)
        dp[0] = 1
        coins = [1, 2, 6]
        for coin in coins:
            for index in range(coin, n + 1):
                dp[index] = (dp[index] + dp[index - coin]) % MODULO
        totalWays = 0
        for count in range(3):
            if count * 4 <= n:
                totalWays = (totalWays + dp[n - count * 4]) % MODULO
        return totalWays