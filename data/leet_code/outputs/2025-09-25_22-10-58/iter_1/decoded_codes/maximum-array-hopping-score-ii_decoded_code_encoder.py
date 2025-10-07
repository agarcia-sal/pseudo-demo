class Solution:
    def maxScore(self, nums):
        n = len(nums)
        dp = [0] * n
        for i in range(n - 2, -1, -1):
            max_score = 0
            for j in range(i + 1, n):
                score = (j - i) * nums[j]
                candidate = score + dp[j]
                if max_score < candidate:
                    max_score = candidate
            dp[i] = max_score
        return dp[0]