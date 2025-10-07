class Solution:
    def waysToReachStair(self, k: int) -> int:
        def dfs(a: int, b: int, c: int) -> int:
            if not (a <= k + 1):
                return 0
            x = (1 if a == k else 0)
            if not (a <= 0 or b != 0):
                x += dfs(a - 1, 1, c)
            x += dfs((a + 1) * 2 * c, 0, c + 1)
            return x
        return dfs(1, 0, 0)