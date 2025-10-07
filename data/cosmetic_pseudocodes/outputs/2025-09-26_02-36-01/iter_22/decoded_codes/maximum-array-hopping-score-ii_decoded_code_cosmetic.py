from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        i = n - 2
        while i >= 0:
            max_val = 0
            j = i + 1
            while j <= n - 1:
                val = (j - i) * nums[j] + dp[j]
                if val > max_val:
                    max_val = val
                j += 1
            dp[i] = max_val
            i -= 1
        return dp[0]