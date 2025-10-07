class Hashing:
    def __init__(self, s, base, mod):
        modValue = mod
        lengthS = len(s)
        self.h = [0] * (lengthS + 1)
        self.p = [1] * (lengthS + 1)
        index = 1
        while index <= lengthS:
            temp1 = self.h[index - 1] * base
            temp2 = ord(s[index - 1])
            sumVal = temp1 + temp2
            self.h[index] = sumVal % modValue
            tempProd = self.p[index - 1] * base
            self.p[index] = tempProd % modValue
            index += 1
        self.mod = modValue

    def query(self, l, r):
        # returns hash of substring s[l-1:r]
        diffVal = self.h[r] - self.h[l - 1] * self.p[r - l + 1]
        result = diffVal % self.mod
        return result


class Solution:
    def findAnswer(self, parent, s):
        n = len(s)
        graph = [[] for _ in range(n)]
        dfsStr = []
        pos = {}

        def dfs(i):
            startPos = len(dfsStr) + 1
            idx = 0
            while idx < len(graph[i]):
                dfs(graph[i][idx])
                idx += 1
            dfsStr.append(s[i])
            endPos = len(dfsStr)
            pos[i] = (startPos, endPos)

        counter = 1
        while counter < n:
            graph[parent[counter]].append(counter)
            counter += 1

        dfs(0)

        base = 33331
        modVal = 998244353
        h1 = Hashing(dfsStr, base, modVal)
        h2 = Hashing(dfsStr[::-1], base, modVal)

        answers = []
        idx = 0
        while idx < n:
            leftBound, rightBound = pos[idx]
            lengthSeg = rightBound - leftBound + 1
            mid = lengthSeg // 2
            if lengthSeg % 2 == 0:
                mid1 = leftBound
                mid2 = leftBound + mid - 1
                val1 = h1.query(mid1, mid2)
                revLeft = n - rightBound + 1
                revRight = revLeft + mid - 1
                val2 = h2.query(revLeft, revRight)
            else:
                val1 = h1.query(leftBound, leftBound + mid - 1) if mid > 0 else 0
                revLeft = n - rightBound + 1
                revRight = revLeft + mid - 1 if mid > 0 else revLeft - 1
                val2 = h2.query(revLeft, revRight) if mid > 0 else 0
            answers.append(val1 == val2)
            idx += 1

        return answers