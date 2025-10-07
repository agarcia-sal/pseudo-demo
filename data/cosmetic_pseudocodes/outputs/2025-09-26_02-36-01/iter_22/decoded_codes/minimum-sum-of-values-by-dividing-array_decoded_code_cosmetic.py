from math import inf
from functools import lru_cache

class Solution:
    def minimumValueSum(self, nums, andValues):
        deltaX = len(nums)
        deltaY = len(andValues)

        @lru_cache(None)
        def dp(alpha, beta):
            def helperAnd(x, y):
                return x & y

            def helperMin(a, b):
                return a if a < b else b

            def baseCase(p, q):
                if q == -1:
                    if p == -1:
                        return 0
                    return inf
                if p == -1:
                    return inf
                return -9999999999

            accMin = inf
            accAnd = -1

            loopIndex = alpha
            while True:
                if accAnd == -1:
                    accAnd = nums[loopIndex]
                else:
                    accAnd = helperAnd(accAnd, nums[loopIndex])
                if accAnd == andValues[beta]:
                    candidate = dp(loopIndex - 1, beta - 1) + nums[alpha]
                    accMin = helperMin(accMin, candidate)
                if loopIndex == -1:
                    break
                loopIndex -= 1

            return accMin

        answer = dp(deltaX - 1, deltaY - 1)
        return answer if answer != inf else -1