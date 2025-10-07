from math import inf
from functools import lru_cache

class Solution:
    def minimumValueSum(self, nums, andValues):
        a = len(nums)
        b = len(andValues)

        @lru_cache(None)
        def dp(x, y):
            if y != -1:
                if x != -1:
                    r = inf
                    q = x
                    p = None  # Use None to indicate uninitialized state
                    while q >= -1:
                        if p is None:
                            p = nums[q]
                        else:
                            p &= nums[q]
                        if p == andValues[y]:
                            temp = dp(q - 1, y - 1)
                            if r > temp + nums[x]:
                                r = temp + nums[x]
                        q -= 1
                    return r
                else:
                    return inf
            else:
                if x == -1:
                    return 0
                else:
                    return inf

        z = dp(a - 1, b - 1)
        return -1 if z == inf else z