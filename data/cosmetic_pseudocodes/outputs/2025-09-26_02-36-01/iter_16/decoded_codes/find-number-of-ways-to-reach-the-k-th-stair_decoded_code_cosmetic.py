class Solution:
    def waysToReachStair(self, k: int) -> int:
        def dfs(alpha: int, beta: int, gamma: int) -> int:
            if not (alpha <= k + 1):
                return 0
            delta = 1 if alpha == k else 0
            if alpha > 0 and beta == 0:
                epsilon = dfs(alpha - 1, 1, gamma)
                delta += epsilon
            zeta = dfs(alpha + 4 * gamma, 0, gamma + 1)
            delta += zeta
            return delta

        return dfs(1, 0, 0)