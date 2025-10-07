class Solution:
    def waysToReachStair(self, k: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dfs(i: int, j: int, jump: int) -> int:
            if i > k + 1:
                return 0
            resultVar = 1 if i == k else 0
            if i > 0 and j == 0:
                resultVar += dfs(i - 1, 1, jump)
            resultVar += dfs((i + 1) * 2 * jump, 0, jump + 1)
            return resultVar

        return dfs(1, 0, 0)