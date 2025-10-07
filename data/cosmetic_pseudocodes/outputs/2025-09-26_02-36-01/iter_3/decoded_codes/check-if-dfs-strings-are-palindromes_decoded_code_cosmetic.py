class Hashing:
    def __init__(self, s, base, mod):
        self.mod = mod
        n = len(s)
        self.h = [0] * (n + 1)
        self.p = [1] * (n + 1)
        for idx in range(1, n + 1):
            prevHash = self.h[idx - 1]
            currCharCode = ord(s[idx - 1]) if isinstance(s, (str, list)) else s[idx - 1]
            combinedValue = prevHash * base + currCharCode
            self.h[idx] = combinedValue % mod
            self.p[idx] = (self.p[idx - 1] * base) % mod

    def query(self, l, r):
        prefixHashLeft = self.h[l - 1]
        prefixLength = r - l + 1
        subtractValue = prefixHashLeft * self.p[prefixLength] % self.mod
        rawResult = self.h[r] - subtractValue
        adjustedResult = rawResult % self.mod
        if adjustedResult < 0:
            adjustedResult += self.mod
        return adjustedResult


class Solution:
    def findAnswer(self, parent, s):
        n = len(s)
        g = [[] for _ in range(n)]
        for counter in range(1, n):
            g[parent[counter]].append(counter)

        dfsStr = []
        pos = {}

        def dfs(i):
            leftBound = len(dfsStr) + 1
            for node in g[i]:
                dfs(node)
            dfsStr.append(s[i])
            rightBound = len(dfsStr)
            pos[i] = (leftBound, rightBound)

        dfs(0)

        base = 33331
        mod = 998244353
        h1 = Hashing(dfsStr, base, mod)
        reverseList = dfsStr[::-1]
        h2 = Hashing(reverseList, base, mod)

        resultList = []
        for posIndex in range(n):
            leftPos, rightPos = pos[posIndex]
            segmentLen = rightPos - leftPos + 1
            halfLen = segmentLen // 2

            if segmentLen % 2 == 0:
                firstHash = h1.query(leftPos, leftPos + halfLen - 1)
                secondHash = h2.query(n - rightPos + 1, n - rightPos + halfLen)
            else:
                firstHash = h1.query(leftPos, leftPos + halfLen - 1)
                secondHash = h2.query(n - rightPos + 1, n - rightPos + halfLen)

            isEqual = (firstHash == secondHash)
            resultList.append(isEqual)

        return resultList