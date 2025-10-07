class Solution:
    def sumOfPower(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Initialize dp array with zeros: dp[i][j] represents the count of subsets from first i elements with sum j
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1  # empty subset sum is 0

        for i in range(1, n + 1):
            num = nums[i - 1]
            for j in range(k + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= num:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - num]) % MOD
                else:
                    dp[i][j] %= MOD

        total_power = 0
        # Iterate over all non-empty subsets using bitmask
        for subset_mask in range(1, 1 << n):
            current_sum = 0
            count = 0
            for j in range(n):
                if (subset_mask >> j) & 1:
                    current_sum += nums[j]
                    count += 1
            if current_sum == k:
                total_power = (total_power + pow(2, n - count, MOD)) % MOD

        return total_power