class Hashing:
    def __init__(self, s, base, mod):
        self.mod = mod
        n = len(s)
        self.h = [0] * (n + 1)
        self.p = [1] * (n + 1)
        for i in range(1, n + 1):
            prevHash = self.h[i - 1]
            charCode = ord(s[i - 1])
            self.h[i] = (prevHash * base + charCode) % mod
            self.p[i] = (self.p[i - 1] * base) % mod

    def query(self, l, r):
        diff = self.h[r] - self.h[l - 1] * self.p[r - l + 1]
        result = diff % self.mod
        return result


class Solution:
    def findAnswer(self, parent, s):
        n = len(s)
        g = [[] for _ in range(n)]
        for j in range(1, n):
            pIdx = parent[j]
            g[pIdx].append(j)

        dfsStr = []
        pos = {}

        def dfs(i):
            leftIdx = len(dfsStr) + 1
            for child in g[i]:
                dfs(child)
            dfsStr.append(s[i])
            rightIdx = len(dfsStr)
            pos[i] = (leftIdx, rightIdx)

        dfs(0)

        base = 33331
        mod = 998244353
        h1 = Hashing(dfsStr, base, mod)
        revStr = dfsStr[::-1]
        h2 = Hashing(revStr, base, mod)

        ans = []
        for x in range(n):
            leftB, rightB = pos[x]
            lengthSub = rightB - leftB + 1
            half = lengthSub // 2
            leftRangeEnd = leftB + half - 1
            rightRangeStart = n - rightB + 1
            rightRangeEnd = rightRangeStart + half - 1
            v1 = h1.query(leftB, leftRangeEnd)
            v2 = h2.query(rightRangeStart, rightRangeEnd)
            res = (v1 == v2)
            ans.append(res)
        return ans