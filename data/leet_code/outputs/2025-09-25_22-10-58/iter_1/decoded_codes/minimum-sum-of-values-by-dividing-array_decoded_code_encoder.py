from math import inf

class Solution:
    def minimumValueSum(self, nums, andValues):
        n = len(nums)
        m = len(andValues)

        from functools import lru_cache

        @lru_cache(None)
        def dp(i, j):
            if j == -1:
                return 0 if i == -1 else inf
            if i == -1:
                return inf

            min_sum = inf
            current_and = -1
            for k in range(i, -2, -1):
                if k == -1:
                    break
                if current_and == -1:
                    current_and = nums[k]
                else:
                    current_and &= nums[k]
                if current_and == andValues[j]:
                    candidate = dp(k - 1, j - 1)
                    if candidate != inf:
                        min_sum = min(min_sum, candidate + nums[i])

            return min_sum

        result = dp(n - 1, m - 1)
        return result if result != inf else -1