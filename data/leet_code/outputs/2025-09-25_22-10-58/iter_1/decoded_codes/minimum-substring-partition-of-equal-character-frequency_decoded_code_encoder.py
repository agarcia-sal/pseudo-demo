from collections import defaultdict

class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)

        def dfs(i: int) -> int:
            if i >= n:
                return 0
            cnt = defaultdict(int)
            freq = defaultdict(int)
            ans = n - i
            for j in range(i, n):
                ch = s[j]
                if cnt[ch] > 0:
                    freq[cnt[ch]] -= 1
                    if freq[cnt[ch]] == 0:
                        del freq[cnt[ch]]
                cnt[ch] += 1
                freq[cnt[ch]] += 1
                if len(freq) == 1:
                    t = 1 + dfs(j + 1)
                    if t < ans:
                        ans = t
            return ans

        return dfs(0)