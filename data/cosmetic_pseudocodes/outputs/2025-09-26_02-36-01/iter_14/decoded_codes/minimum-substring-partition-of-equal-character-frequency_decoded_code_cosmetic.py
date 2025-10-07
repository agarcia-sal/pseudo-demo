from collections import defaultdict

class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        def dfs(k: int) -> int:
            if k >= len(s):
                return 0
            u = defaultdict(int)
            v = defaultdict(int)
            r = len(s) - k
            m = k
            while m < len(s):
                if u[s[m]] != 0:
                    w = u[s[m]]
                    v[w] -= 1
                    if v[w] == 0:
                        del v[w]
                u[s[m]] += 1
                x = u[s[m]]
                v[x] = v.get(x, 0) + 1
                if len(v) == 1:
                    y = dfs(m + 1) + 1
                    if y < r:
                        r = y
                m += 1
            return r
        return dfs(0)