class Hashing:
    def __init__(self, s, base, mod):
        self.mod = mod
        n = len(s)
        self.h = [0] * (n + 1)
        self.p = [1] * (n + 1)
        x = 1
        while x <= n:
            prevHash = self.h[x - 1]
            chCode = ord(s[x - 1])
            mul = (prevHash * base)
            sumVal = mul + chCode
            self.h[x] = sumVal % mod
            self.p[x] = (self.p[x - 1] * base) % mod
            x += 1

    def query(self, l, r):
        diff = self.h[r] - (self.h[l - 1] * self.p[r - l + 1])
        result = diff % self.mod
        if result < 0:
            result += self.mod
        return result


class Solution:
    def findAnswer(self, parent, s):
        n = len(s)
        g = [[] for _ in range(n)]
        idx = 1
        while idx < n:
            pIdx = parent[idx]
            g[pIdx].append(idx)
            idx += 1

        dfsStr = []
        pos = {}

        def dfs(i):
            startPos = len(dfsStr) + 1
            for child in g[i]:
                dfs(child)
            dfsStr.append(s[i])
            endPos = len(dfsStr)
            pos[i] = (startPos, endPos)

        dfs(0)

        baseVal = 33331
        modVal = 998244353
        h1 = Hashing(dfsStr, baseVal, modVal)
        reversedDfsStr = []
        revIdx = len(dfsStr)
        while revIdx >= 1:
            reversedDfsStr.append(dfsStr[revIdx - 1])
            revIdx -= 1
        h2 = Hashing(reversedDfsStr, baseVal, modVal)

        answerList = []
        posIdx = 0
        while posIdx < n:
            interval = pos[posIdx]
            leftBound = interval[0]
            rightBound = interval[1]
            lengthVal = rightBound - leftBound + 1
            half = lengthVal // 2
            if lengthVal % 2 == 0:
                firstHalfHash = h1.query(leftBound, leftBound + half - 1)
                secondHalfHash = h2.query(
                    n - rightBound + 1,
                    n - rightBound + 1 + half - 1,
                )
            else:
                firstHalfHash = h1.query(leftBound, leftBound + half - 1)
                secondHalfHash = h2.query(
                    n - rightBound + 1,
                    n - rightBound + 1 + half - 1,
                )
            answerList.append(firstHalfHash == secondHalfHash)
            posIdx += 1

        return answerList