class Solution:
    def maxScore(self, nums):
        length = len(nums)
        dp = [0] * length
        dp[0] = 0
        index = 1
        while index < length:
            inner = 0
            while inner < index:
                candidate = dp[inner] + ((index - inner) * nums[index])
                if dp[index] < candidate:
                    dp[index] = candidate
                inner += 1
            index += 1
        return dp[length - 1]