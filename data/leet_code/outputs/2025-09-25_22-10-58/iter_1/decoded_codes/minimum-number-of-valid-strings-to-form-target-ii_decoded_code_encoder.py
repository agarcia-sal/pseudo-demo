class Solution:
    def minValidStrings(self, words, target):
        prefixes = set()
        for word in words:
            for i in range(1, len(word) + 1):
                prefixes.add(word[:i])
        n = len(target)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                if target[j-1:i] in prefixes:
                    dp[i] = min(dp[i], dp[j-1] + 1)
        return dp[n] if dp[n] != float('inf') else -1