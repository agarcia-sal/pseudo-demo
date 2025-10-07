class Hashing:
    def __init__(self, s, base, mod):
        self.mod = mod
        size = len(s)
        self.h = [0] * (size + 1)
        self.p = [1] * (size + 1)
        for idx in range(1, size + 1):
            temp1 = self.h[idx - 1] * base
            temp2 = ord(s[idx - 1])  # Unicode code point of character
            self.h[idx] = (temp1 + temp2) % mod
            self.p[idx] = (self.p[idx - 1] * base) % mod

    def query(self, l, r):
        part1 = self.h[r]
        part2 = (self.h[l - 1] * self.p[r - l + 1]) % self.mod
        result = (part1 - part2 + self.mod) % self.mod
        return result


class Solution:
    def findAnswer(self, parent, s):
        n = len(s)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            p = parent[i]
            g[p].append(i)

        dfsStr = []
        pos = {}

        def dfs(idx):
            left = len(dfsStr) + 1  # 1-based index for hashing
            for childElement in g[idx]:
                dfs(childElement)
            dfsStr.append(s[idx])
            right = len(dfsStr)
            pos[idx] = (left, right)

        dfs(0)

        base = 33331
        mod = 998244353
        h1 = Hashing(dfsStr, base, mod)

        reversedStr = dfsStr[::-1]
        h2 = Hashing(reversedStr, base, mod)

        results = []
        for index in range(n):
            leftBound, rightBound = pos[index]
            lengthSub = rightBound - leftBound + 1
            halfLen = lengthSub // 2
            val1 = h1.query(leftBound, leftBound + halfLen - 1)
            val2 = h2.query(n - rightBound + 1, n - rightBound + halfLen)
            results.append(val1 == val2)

        return results