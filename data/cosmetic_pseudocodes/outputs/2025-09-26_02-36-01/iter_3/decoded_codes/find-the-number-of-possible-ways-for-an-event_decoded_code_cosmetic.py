class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        modulus = 10**9 + 7
        dp = [[0] * (x + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for indexI in range(1, n + 1):
            for indexJ in range(1, x + 1):
                temp1 = dp[indexI - 1][indexJ] * indexJ
                temp2 = dp[indexI - 1][indexJ - 1] * (x - indexJ - 1)
                dp[indexI][indexJ] = (temp1 + temp2) % modulus

        result = 0
        powerVal = 1
        for counter in range(1, x + 1):
            powerVal = (powerVal * y) % modulus
            result = (result + dp[n][counter] * powerVal) % modulus

        return result