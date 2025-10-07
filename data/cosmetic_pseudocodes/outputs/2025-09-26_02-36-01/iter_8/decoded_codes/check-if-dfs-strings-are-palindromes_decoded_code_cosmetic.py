class Hashing:
    def __init__(self, s, base, mod):
        self.mod = mod
        n = len(s)
        self.h = [0] * (n + 1)
        self.p = [1] * (n + 1)
        for idx in range(1, n + 1):
            prev_hash = self.h[idx - 1]
            char_code = ord(s[idx - 1])
            combined_sum = prev_hash * base + char_code
            self.h[idx] = combined_sum % mod
            prev_pow = self.p[idx - 1]
            self.p[idx] = (prev_pow * base) % mod

    def query(self, l, r):
        diff_hash = self.h[r] - (self.h[l - 1] * self.p[r - l + 1])
        result = (diff_hash % self.mod + self.mod) % self.mod
        return result


class Solution:
    def findAnswer(self, parent, s):
        sizeVal = len(s)
        g = [[] for _ in range(sizeVal)]
        for idx in range(1, sizeVal):
            pVal = parent[idx]
            g[pVal].append(idx)

        dfsStr = []
        pos = {}

        def dfs(i):
            startIdx = len(dfsStr) + 1
            for childIdx in g[i]:
                dfs(childIdx)
            dfsStr.append(s[i])
            endIdx = len(dfsStr)
            pos[i] = (startIdx, endIdx)

        dfs(0)

        baseVal = 33000 + 331
        modVal = 998000000 + 24353
        h1 = Hashing(dfsStr, baseVal, modVal)

        reversedStr = dfsStr[::-1]
        h2 = Hashing(reversedStr, baseVal, modVal)

        answers = []
        for loopIndex in range(sizeVal):
            leftBound, rightBound = pos[loopIndex]
            lengthK = rightBound - leftBound + 1
            halfK = lengthK // 2
            isEven = (lengthK % 2) == 0
            if isEven:
                val1 = h1.query(leftBound, leftBound + halfK - 1)
                val2 = h2.query(sizeVal - rightBound + 1, sizeVal - rightBound + halfK)
            else:
                val1 = h1.query(leftBound, leftBound + halfK - 1)
                val2 = h2.query(sizeVal - rightBound + 1, sizeVal - rightBound + halfK)
            answers.append(val1 == val2)

        return answers