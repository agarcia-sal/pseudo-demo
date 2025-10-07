class Solution:
    def waysToReachStair(self, k: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dfs(i: int, j: int, jump: int) -> int:
            if i > k + 1:
                return 0

            resultVal = 1 if i == k else 0

            if i > 0 and j == 0:
                resultVal += dfs(i - 1, 1, jump)

            incStep = jump + 1
            nextIndex = i + 2 * jump
            resultVal += dfs(nextIndex, 0, incStep)

            return resultVal

        return dfs(1, 0, 0)