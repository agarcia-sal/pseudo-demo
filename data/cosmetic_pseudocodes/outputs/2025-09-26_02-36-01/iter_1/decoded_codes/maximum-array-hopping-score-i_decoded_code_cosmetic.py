from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [0] * length
        dp[0] = 0
        for index in range(1, length):
            for prev in range(index):
                potential = dp[prev] + (index - prev) * nums[index]
                if dp[index] < potential:
                    dp[index] = potential
        return dp[length - 1]