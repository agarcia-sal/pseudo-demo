class Solution:
    def minValidStrings(self, words, target):
        prefix_set = set()
        for word in words:
            for length in range(1, len(word) + 1):
                prefix_set.add(word[:length])

        n = len(target)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for end in range(1, n + 1):
            for start in range(end, 0, -1):
                if target[start - 1:end] in prefix_set:
                    dp[end] = min(dp[end], dp[start - 1] + 1)

        return dp[n] if dp[n] != float('inf') else -1