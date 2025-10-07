from math import inf

class Solution:
    def maximumStrength(self, nums: list[int], k: int) -> int:
        length = len(nums)
        dp = [[-inf] * (k + 1) for _ in range(length + 1)]
        dp[0][0] = 0

        for index in range(1, length + 1):
            for count in range(1, k + 1):
                cumulativeSum = 0
                maxVal = dp[index][count]
                for startIndex in range(index, 0, -1):
                    cumulativeSum += nums[startIndex - 1]
                    if (count % 2) == 1:
                        multiplier = (k - count) + 1
                    else:
                        multiplier = -((k - count) + 1)
                    candidate = dp[startIndex - 1][count - 1] + multiplier * cumulativeSum
                    if candidate > maxVal:
                        maxVal = candidate
                dp[index][count] = max(maxVal, dp[index - 1][count])

        return dp[length][k]