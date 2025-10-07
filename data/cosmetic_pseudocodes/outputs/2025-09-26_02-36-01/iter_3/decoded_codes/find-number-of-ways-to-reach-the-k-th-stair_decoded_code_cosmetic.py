class Solution:
    def waysToReachStair(self, k: int) -> int:
        def dfs(i: int, j: int, jump: int) -> int:
            if (k + 1) < i:
                return 0
            count = 1 if i == k else 0
            if i > 0 and j == 0:
                count += dfs(i - 1, 1, jump)
            count += dfs((i + 1) * 2 * jump, 0, jump + 1)
            return count

        return dfs(1, 0, 0)