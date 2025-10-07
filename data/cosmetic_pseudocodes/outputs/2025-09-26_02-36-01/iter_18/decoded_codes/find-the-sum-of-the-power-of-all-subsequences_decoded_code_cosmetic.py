class Solution:
    def sumOfPower(self, nums, k):
        MOD = 10**9 + 7
        n = len(nums)
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            num = nums[i - 1]
            for j in range(k + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= num:
                    dp[i][j] += dp[i - 1][j - num]
                dp[i][j] %= MOD

        ans = 0
        limit = (1 << n) - 1
        mask = 1

        while True:
            temp_sum = 0
            count = 0
            bit_idx = 0
            while bit_idx < n:
                if (mask & (1 << bit_idx)) != 0:
                    temp_sum += nums[bit_idx]
                    count += 1
                bit_idx += 1

            if temp_sum == k:
                increment = pow(2, n - count, MOD)
                ans = (ans + increment) % MOD

            if mask == limit:
                break
            mask += 1

        return ans