class Solution:
    def countOfPairs(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        max_val = max(nums)

        dp = [[[0] * (max_val + 1) for _ in range(max_val + 1)] for _ in range(n)]

        for j in range(nums[0] + 1):
            k = nums[0] - j
            dp[0][j][k] = 1

        for i in range(1, n):
            val = nums[i]
            for j in range(val + 1):
                k = val - j
                for j_prev in range(j + 1):
                    for k_prev in range(k, max_val + 1):
                        dp[i][j][k] = (dp[i][j][k] + dp[i - 1][j_prev][k_prev]) % MOD

        result = 0
        last_val = nums[-1]
        for j in range(max_val + 1):
            for k in range(max_val + 1):
                if j + k == last_val:
                    result = (result + dp[-1][j][k]) % MOD

        return result