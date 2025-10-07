from math import inf
from functools import lru_cache

class Solution:
    def minimumValueSum(self, nums, andValues):
        a = len(nums)
        b = len(andValues)

        @lru_cache(None)
        def dp(x, y):
            def helper(p, q):
                if q == -1:
                    return 0 if p == -1 else inf
                if p == -1:
                    return inf

                z = inf
                r = -1

                def helperLoop(u, r_val, best):
                    if u < 0:
                        return best
                    if r_val == -1:
                        r_val = nums[u]
                    else:
                        r_val &= nums[u]
                    if r_val == andValues[q]:
                        w = dp(u - 1, q - 1) + nums[p]
                        if w < best:
                            best = w
                    return helperLoop(u - 1, r_val, best)

                z = helperLoop(p, r, z)
                return z

            return helper(x, y)

        output = dp(a - 1, b - 1)
        return output if output != inf else -1