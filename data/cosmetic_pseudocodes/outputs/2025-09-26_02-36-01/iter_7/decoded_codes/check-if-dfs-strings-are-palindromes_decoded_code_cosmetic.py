class Hashing:
    def __init__(self, s, base, mod):
        moduloBase = mod
        n = len(s)
        hashArray = [0] * (n + 1)
        powerArray = [1] * (n + 1)
        for index in range(1, n + 1):
            leftHash = hashArray[index - 1]
            charValue = ord(s[index - 1])
            combinedHash = (leftHash * base + charValue) % moduloBase
            hashArray[index] = combinedHash
            powerArray[index] = (powerArray[index - 1] * base) % moduloBase
        self.mod = moduloBase
        self.h = hashArray
        self.p = powerArray

    def query(self, l, r):
        modVal = self.mod
        hashR = self.h[r]
        hashLMinusOne = self.h[l - 1]
        powerLen = self.p[r - l + 1]
        result = (hashR - (hashLMinusOne * powerLen) % modVal + modVal) % modVal
        return result


class Solution:
    def findAnswer(self, parent, s):
        lengthStr = len(s)
        graph = [[] for _ in range(lengthStr)]
        for idxLoop in range(1, lengthStr):
            pVal = parent[idxLoop]
            graph[pVal].append(idxLoop)

        dfsStr = []
        pos = {}

        def dfs(i):
            leftBound = len(dfsStr) + 1
            for childElement in graph[i]:
                dfs(childElement)
            dfsStr.append(s[i])
            rightBound = len(dfsStr)
            pos[i] = (leftBound, rightBound)

        dfs(0)

        BASE_CONST = 30000 + 3331
        MOD_CONST = 998000000 + 244353
        hShash = Hashing(dfsStr, BASE_CONST, MOD_CONST)
        hRhash = Hashing(dfsStr[::-1], BASE_CONST, MOD_CONST)

        resultList = []
        for iterator in range(lengthStr):
            leftLimit, rightLimit = pos[iterator]
            rangeLen = rightLimit - leftLimit + 1

            if (rangeLen % 2) == 0:
                halfLen = rangeLen // 2
                firstVal = hShash.query(leftLimit, leftLimit + halfLen - 1)
                secondVal = hRhash.query(lengthStr - rightLimit + 1, lengthStr - rightLimit + 1 + halfLen - 1)
            else:
                halfLen = (rangeLen // 2) + 0
                # The pseudocode expression is equivalent to leftLimit + floor(rangeLen/2)
                firstVal = hShash.query(leftLimit, leftLimit + (rangeLen // 2))
                right_start = lengthStr - rightLimit + 1
                right_end = right_start + (rangeLen // 2)
                secondVal = hRhash.query(right_start, right_end)
                if secondVal is None:
                    secondVal = 0

            isEqual = (firstVal == secondVal)
            resultList.append(isEqual)

        return resultList