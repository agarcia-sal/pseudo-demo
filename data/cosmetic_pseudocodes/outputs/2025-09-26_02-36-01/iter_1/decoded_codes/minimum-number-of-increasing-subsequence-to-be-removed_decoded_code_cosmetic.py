class Solution:
    def minOperations(self, nums):
        length = len(nums)
        if length == 0:
            return 0
        dp = [1] * length
        for current in range(1, length):
            for previous in range(current):
                if nums[current] <= nums[previous]:
                    dp[current] = max(dp[current], dp[previous] + 1)
        result = dp[0]
        for val in dp:
            if val > result:
                result = val
        return result