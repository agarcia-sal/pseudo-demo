from math import inf
from functools import lru_cache

class Solution:
    def minimumValueSum(self, nums, andValues):
        n, m = len(nums), len(andValues)

        @lru_cache(None)
        def dp(i, j):
            if j == -1:
                return 0 if i == -1 else inf
            if i == -1:
                return inf

            res = inf
            w = -1

            def recurse(k):
                nonlocal w, res
                if k < -1:
                    return
                if w == -1:
                    w = nums[k]
                else:
                    w &= nums[k]

                if w == andValues[j]:
                    val = dp(k - 1, j - 1) + nums[i]
                    if val < res:
                        res = val
                recurse(k - 1)

            recurse(i)
            return res

        ans = dp(n - 1, m - 1)
        return ans if ans != inf else -1