from math import inf
from functools import lru_cache

class Solution:
    def minimumValueSum(self, nums, andValues):
        totalNums = len(nums)
        totalAnds = len(andValues)

        @lru_cache(None)
        def dp(i, j):
            if j < 0:
                if i < 0:
                    return 0
                else:
                    return inf
            if i < 0:
                return inf

            minSum = inf
            accAnd = -1
            idx = i
            while idx >= -1:
                if accAnd == -1:
                    if idx < 0:
                        break
                    accAnd = nums[idx]
                else:
                    if idx < 0:
                        break
                    accAnd &= nums[idx]

                if accAnd == andValues[j]:
                    tempValue = dp(idx - 1, j - 1) + nums[i]
                    if tempValue < minSum:
                        minSum = tempValue
                idx -= 1

            return minSum

        answer = dp(totalNums - 1, totalAnds - 1)
        return answer if answer != inf else -1