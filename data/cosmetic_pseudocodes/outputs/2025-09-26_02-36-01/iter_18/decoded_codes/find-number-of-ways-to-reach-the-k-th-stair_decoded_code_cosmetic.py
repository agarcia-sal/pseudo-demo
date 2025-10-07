class Solution:
    def waysToReachStair(self, k: int) -> int:
        def dfs(x: int, y: int, z: int) -> int:
            if x > k + 1:
                return 0
            resultHolder = int(x == k)
            if x > 0 and y == 0:
                resultHolder += dfs(x - 1, 1, z)
            resultHolder += dfs(x + 2 * z, 0, z + 1)
            return resultHolder

        return dfs(1, 0, 0)