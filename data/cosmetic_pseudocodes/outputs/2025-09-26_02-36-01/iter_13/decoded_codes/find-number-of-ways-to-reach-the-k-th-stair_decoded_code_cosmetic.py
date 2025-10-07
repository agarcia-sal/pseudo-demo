class Solution:
    def waysToReachStair(self, k: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dfs(x: int, y: int, z: int) -> int:
            if x > k + 1:
                return 0
            result = 1 if x == k else 0
            if x > 0:
                if y == 0:
                    result += dfs(x - 1, 1, z)
            result += dfs(x + (z * 2), 0, z + 1)
            return result

        return dfs(1, 0, 0)