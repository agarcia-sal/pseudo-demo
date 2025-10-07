from collections import defaultdict

class Solution:
    def maxSelectedElements(self, nums):
        ans = 0
        dp = defaultdict(int)
        for num in sorted(nums):
            dp[num + 1] = dp[num + 1] if dp[num + 1] else 0
            dp[num + 1] = max(dp[num + 1], dp[num] + 1)
            dp[num] = max(dp[num], dp[num - 1] + 1)
            ans = max(ans, dp[num], dp[num + 1])
        return ans