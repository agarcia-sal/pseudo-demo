from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [0] * length
        for index in range(length - 2, -1, -1):
            highest_score = 0
            for next_index in range(index + 1, length):
                current_score = (next_index - index) * nums[next_index]
                total_score = current_score + dp[next_index]
                if total_score > highest_score:
                    highest_score = total_score
            dp[index] = highest_score
        return dp[0]