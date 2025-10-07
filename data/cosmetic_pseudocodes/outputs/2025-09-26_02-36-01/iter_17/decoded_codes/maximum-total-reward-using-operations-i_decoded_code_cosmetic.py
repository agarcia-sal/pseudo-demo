from bisect import bisect_right
from functools import lru_cache

class Solution:
    def maxTotalReward(self, rewardValues):
        rewardValues.sort()
        n = len(rewardValues)

        @lru_cache(None)
        def dfs(y):
            # Find insertion point where rewardValues[m] > y using binary search
            q = bisect_right(rewardValues, y)
            r = 0
            for s in range(q, n):
                w = rewardValues[s]
                t = y + w
                if t > y:  # always true for positive w, but keep for consistency
                    u = dfs(t)
                    if r < w + u:
                        r = w + u
            return r

        return dfs(0)