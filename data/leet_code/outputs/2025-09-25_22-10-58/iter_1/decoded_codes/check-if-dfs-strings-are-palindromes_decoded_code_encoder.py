class Hashing:
    def __init__(self, s, base, mod):
        self.mod = mod
        n = len(s)
        self.h = [0] * (n + 1)
        self.p = [1] * (n + 1)
        for i in range(1, n + 1):
            self.h[i] = (self.h[i - 1] * base + ord(s[i - 1])) % mod
            self.p[i] = (self.p[i - 1] * base) % mod

    def query(self, l, r):
        return (self.h[r] - self.h[l - 1] * self.p[r - l + 1]) % self.mod


class Solution:
    def findAnswer(self, parent, s):
        n = len(s)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[parent[i]].append(i)

        dfsStr = []
        pos = {}

        def dfs(i):
            l = len(dfsStr) + 1
            for j in g[i]:
                dfs(j)
            dfsStr.append(s[i])
            r = len(dfsStr)
            pos[i] = (l, r)

        dfs(0)

        base = 33331
        mod = 998244353

        h1 = Hashing(dfsStr, base, mod)
        h2 = Hashing(dfsStr[::-1], base, mod)

        ans = []
        for i in range(n):
            l, r = pos[i]
            k = r - l + 1
            half = k // 2
            if k % 2 == 0:
                v1 = h1.query(l, l + half - 1)
                v2 = h2.query(n - r + 1, n - r + half)
            else:
                v1 = h1.query(l, l + half - 1)
                v2 = h2.query(n - r + 1, n - r + half)
            ans.append(v1 == v2)

        return ans