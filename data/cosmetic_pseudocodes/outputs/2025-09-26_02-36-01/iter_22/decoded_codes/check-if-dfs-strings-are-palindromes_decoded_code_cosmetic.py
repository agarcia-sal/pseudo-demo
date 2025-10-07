class Hashing:
    def __init__(self, s, base, mod):
        self.mod = mod
        self.p = []
        self.h = []
        m = len(s) + 1
        for idx in range(m):
            if idx == 0:
                self.p.append(1)
                self.h.append(0)
            else:
                x = (self.h[idx - 1] * base + ord(s[idx - 1])) % mod
                self.h.append(x)
                y = (self.p[idx - 1] * base) % mod
                self.p.append(y)

    def query(self, l, r):
        diff = self.h[r] - (self.h[l - 1] * self.p[r - l + 1])
        return (diff % self.mod + self.mod) % self.mod


class Solution:
    def findAnswer(self, parent, s):
        n = len(s)
        g = [[] for _ in range(n)]
        for x in range(1, n):
            g[parent[x]].append(x)

        dfsStr = []
        pos = {}

        def dfs(i):
            startPos = len(dfsStr) + 1
            for node in g[i]:
                dfs(node)
            dfsStr.append(s[i])
            endPos = len(dfsStr)
            pos[i] = (startPos, endPos)

        dfs(0)

        base = 33331
        mod = 998244353
        h1 = Hashing(dfsStr, base, mod)
        reversedStr = dfsStr[::-1]
        h2 = Hashing(reversedStr, base, mod)

        ans = []
        for i in range(n):
            l, r = pos[i]
            lengthVal = r - l + 1
            if lengthVal % 2 == 0:
                halfLen = lengthVal // 2
                val1 = h1.query(l, l + halfLen - 1)
                val2 = h2.query(n - r + 1, n - r + halfLen)
            else:
                halfLen = (lengthVal - 1) // 2
                val1 = h1.query(l, l + halfLen)
                val2 = h2.query(n - r + 1, n - r + halfLen + 1)
            ans.append(val1 == val2)

        return ans