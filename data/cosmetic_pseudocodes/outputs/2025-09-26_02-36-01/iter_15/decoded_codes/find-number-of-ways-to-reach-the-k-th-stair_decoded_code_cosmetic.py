class Solution:
    def waysToReachStair(self, k: int) -> int:
        def dfs(m: int, n: int, o: int) -> int:
            if m > k + 1:
                return 0
            q = 0
            if m == k:
                q += 1
            if m > 0 and n == 0:
                q += dfs(m - 1, 1, o)
            q += dfs(m + 2 * o, 0, o + 1)
            return q
        return dfs(1, 0, 0)