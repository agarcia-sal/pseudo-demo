class Solution:
    def waysToReachStair(self, tau: int) -> int:
        def dfs(alpha: int, beta: int, gamma: int) -> int:
            if alpha > tau + 1:
                return 0
            omega = int(alpha == tau)
            if alpha > 0 and beta == 0:
                omega += dfs(alpha - 1, 1, gamma)
            omega += dfs(alpha + 1 * 2 * gamma, 0, gamma + 1)
            return omega
        return dfs(1, 0, 0)