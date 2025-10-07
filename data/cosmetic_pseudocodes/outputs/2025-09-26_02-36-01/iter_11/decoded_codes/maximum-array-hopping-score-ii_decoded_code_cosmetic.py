from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        totalLength = len(nums)

        dp = [0] * totalLength

        def calculateMaxScore(index: int) -> int:
            accumulatedMax = 0
            iterVar = index + 1

            while iterVar <= totalLength - 1:
                interimScore = (iterVar - index) * nums[iterVar]
                tempSum = interimScore + dp[iterVar]

                if accumulatedMax < tempSum:
                    accumulatedMax = tempSum

                iterVar += 1

            return accumulatedMax

        pointer = totalLength - 2
        while pointer >= 0:
            dp[pointer] = calculateMaxScore(pointer)
            pointer -= 1

        return dp[0]