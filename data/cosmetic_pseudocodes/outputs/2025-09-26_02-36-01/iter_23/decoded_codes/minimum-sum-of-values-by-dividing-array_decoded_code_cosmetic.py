from math import inf
from functools import lru_cache

class Solution:
    def minimumValueSum(self, nums, andValues):
        a = len(nums)
        b = len(andValues)

        @lru_cache(None)
        def dp(x, y):
            if y == -1:
                return 0 if x == -1 else inf
            if x == -1:
                return inf

            valMin = inf
            valCur = -1

            def recurse(k):
                nonlocal valCur, valMin
                if k < -1:
                    return
                if valCur == -1:
                    valCur = nums[k]
                else:
                    valCur &= nums[k]
                if valCur == andValues[y]:
                    tempSum = dp(k - 1, y - 1) + nums[x]
                    if tempSum < valMin:
                        valMin = tempSum
                recurse(k - 1)

            recurse(x)
            return valMin

        output = dp(a - 1, b - 1)
        return output if output != inf else -1