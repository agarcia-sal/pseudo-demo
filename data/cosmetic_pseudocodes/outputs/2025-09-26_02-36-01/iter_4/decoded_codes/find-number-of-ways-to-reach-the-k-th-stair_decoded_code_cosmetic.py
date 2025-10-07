class Solution:
    def waysToReachStair(self, k: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dfs(i: int, j: int, jump: int) -> int:
            if i > k + 1:
                return 0

            result = int(i == k)

            if i > 0:
                if j == 0:
                    result += dfs(i - 1, 1, jump)

            incrementStep = 2 * jump
            nextI = i + incrementStep
            nextJump = jump + 1

            result += dfs(nextI, 0, nextJump)
            return result

        return dfs(1, 0, 0)