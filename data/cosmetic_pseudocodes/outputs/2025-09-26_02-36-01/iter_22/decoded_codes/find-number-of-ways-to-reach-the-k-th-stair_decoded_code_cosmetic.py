class Solution:
    def waysToReachStair(self, k: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dfs(x: int, y: int, z: int) -> int:
            if x > k + 1:
                return 0
            result = 0
            if x == k:
                result = 1
            if x > 0 and y == 0:
                result += dfs(x - 1, 1, z)
            result += dfs(x + 2 * z, 0, z + 1)
            return result

        return dfs(1, 0, 0)