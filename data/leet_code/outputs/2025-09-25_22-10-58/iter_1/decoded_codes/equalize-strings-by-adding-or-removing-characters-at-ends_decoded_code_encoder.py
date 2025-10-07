class Solution:
    def minOperations(self, initial: str, target: str) -> int:
        m, n = len(initial), len(target)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_lcs = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if initial[i - 1] == target[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    if dp[i][j] > max_lcs:
                        max_lcs = dp[i][j]

        return m + n - 2 * max_lcs