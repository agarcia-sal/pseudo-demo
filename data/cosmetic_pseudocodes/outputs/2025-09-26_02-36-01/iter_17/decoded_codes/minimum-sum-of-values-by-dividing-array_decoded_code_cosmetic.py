from math import inf

class Solution:
    def minimumValueSum(self, nums, andValues):
        a = len(nums)
        b = len(andValues)

        from functools import lru_cache

        @lru_cache(None)
        def dp(x, y):
            if y == -1:
                return 0 if x == -1 else inf
            if x == -1:
                return inf

            z = inf
            w = -1
            idx = x
            while idx >= -1:
                if w == -1:
                    if idx == -1:
                        break  # avoid index error
                    w = nums[idx]
                else:
                    if idx == -1:
                        break
                    w &= nums[idx]

                if w == andValues[y]:
                    temp = dp(idx - 1, y - 1)
                    temp2 = temp + nums[x]
                    if temp2 < z:
                        z = temp2
                idx -= 1
            return z

        output = dp(a - 1, b - 1)
        if output != inf:
            return output
        else:
            return -1