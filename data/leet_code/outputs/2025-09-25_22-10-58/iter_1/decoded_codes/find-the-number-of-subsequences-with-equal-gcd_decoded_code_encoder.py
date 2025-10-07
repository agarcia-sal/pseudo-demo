from math import gcd

class Solution:
    def subsequencePairCount(self, nums):
        MOD = 10**9 + 7
        maxNum = max(nums)
        dp = [[0] * (maxNum + 1) for _ in range(maxNum + 1)]
        dp[0][0] = 1

        for num in nums:
            newDp = [[0] * (maxNum + 1) for _ in range(maxNum + 1)]
            for x in range(maxNum + 1):
                for y in range(maxNum + 1):
                    val = dp[x][y]
                    if val == 0:
                        continue  # skip zero values for efficiency
                    newDp[x][y] = (newDp[x][y] + val) % MOD

                    newX = gcd(x, num)
                    newDp[newX][y] = (newDp[newX][y] + val) % MOD

                    newY = gcd(y, num)
                    newDp[x][newY] = (newDp[x][newY] + val) % MOD
            dp = newDp

        result = 0
        for g in range(1, maxNum + 1):
            result += dp[g][g]
        return result % MOD