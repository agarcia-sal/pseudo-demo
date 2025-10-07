from typing import List

class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        dp = {}
        ans = 0
        sortedNums = sorted(nums)
        for num in sortedNums:
            valNext = dp.get(num + 1, 0)
            valPrev = dp.get(num - 1, 0)

            dp[num + 1] = valNext + 1
            dp[num] = valPrev + 1

            ans = max(ans, dp[num], dp[num + 1])
        return ans