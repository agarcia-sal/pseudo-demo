class Solution:
    def waysToReachStair(self, k: int) -> int:
        def dfs(x: int, y: int, z: int) -> int:
            if (k + 1) < x:
                return 0
            omega = 1 if x == k else 0
            if x > 0 and y == 0:
                phi = dfs(x - 1, 1, z)
                omega += phi
            psi = dfs(x + (2 * z), 0, z + 1)
            omega += psi
            return omega

        result = dfs(1, 0, 0)
        return result