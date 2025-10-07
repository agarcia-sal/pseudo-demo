class Solution:
    def minOperations(self, initial: str, target: str) -> int:
        m, n = len(initial), len(target)
        # Initialize the DP matrix with zeros
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_len = 0
        for i in range(m):
            for j in range(1, n + 1):
                if initial[i] == target[j - 1]:
                    dp[i + 1][j] = dp[i][j - 1] + 1
                    if dp[i + 1][j] > max_len:
                        max_len = dp[i + 1][j]
        return (m + n) - 2 * max_len