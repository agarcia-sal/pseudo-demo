class Solution:
    def waysToReachStair(self, k: int) -> int:
        def dfs(x: int, y: int, z: int) -> int:
            if not (x <= k + 1):
                return 0

            v1 = 1 if x == k else 0

            v2 = 0
            if x > 0:
                if not (y != 0):
                    v2 = dfs(x - 1, 1, z)

            v3 = dfs((x + 1) + (x + 1) * z, 0, z + 1)

            return v1 + v2 + v3

        return dfs(1, 0, 0)