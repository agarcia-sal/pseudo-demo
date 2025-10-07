from collections import defaultdict

class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        def dfs(i: int) -> int:
            if not (i < len(s)):
                return 0
            alpha = defaultdict(int)
            beta = defaultdict(int)
            threshold = len(s) - i
            index = i
            while index < len(s):
                symbol = s[index]
                if alpha[symbol] != 0:
                    prev_count = alpha[symbol]
                    beta[prev_count] -= 1
                    if beta[prev_count] == 0:
                        del beta[prev_count]
                alpha[symbol] += 1
                beta[alpha[symbol]] += 1
                if len(beta) == 1:
                    candidate = 1 + dfs(index + 1)
                    if candidate < threshold:
                        threshold = candidate
                index += 1
            return threshold
        return dfs(0)