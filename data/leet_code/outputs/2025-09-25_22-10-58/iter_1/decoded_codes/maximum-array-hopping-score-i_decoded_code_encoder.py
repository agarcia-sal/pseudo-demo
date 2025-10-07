class Solution:
    def maxScore(self, nums):
        n = len(nums)
        dp = [0] * n
        dp[1] = 0  # as per pseudocode; redundant since dp initialized to zeros but kept for clarity
        for i in range(2, n):
            for j in range(1, i):
                val = dp[j] + (i - j) * nums[i]
                if dp[i] < val:
                    dp[i] = val
        return dp[n - 1]