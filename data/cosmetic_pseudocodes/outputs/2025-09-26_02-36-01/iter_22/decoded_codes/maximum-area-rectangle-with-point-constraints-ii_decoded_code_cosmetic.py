from bisect import bisect_left

class Fenwick:
    def __init__(self, n):
        self.tree = [0] * (n + 1)

    def add(self, i):
        while i < len(self.tree):
            self.tree[i] += 1
            i += i & -i

    def pre(self, i):
        accumulator = 0
        while i > 0:
            accumulator += self.tree[i]
            i &= i - 1
        return accumulator

    def query(self, l, r):
        return self.pre(r) - self.pre(l - 1)


class Solution:
    def maxRectangleArea(self, xCoord, yCoord):
        pairedList = sorted(zip(xCoord, yCoord))
        uniqueYs = sorted(set(yCoord))
        result = -1
        indexTree = Fenwick(len(uniqueYs))
        indexTree.add(bisect_left(uniqueYs, pairedList[0][1]) + 1)
        record = {}

        def processPairs(pList):
            nonlocal result
            if len(pList) == 1:
                return
            firstPair = pList[0]
            secondPair = pList[1]
            xOne, yOne = firstPair
            xTwo, yTwo = secondPair
            mappedY = bisect_left(uniqueYs, yTwo) + 1
            indexTree.add(mappedY)
            if xOne != xTwo:
                processPairs(pList[1:])
                return
            intervalSum = indexTree.query(bisect_left(uniqueYs, yOne) + 1, mappedY)
            if yTwo in record and record[yTwo][1] == yOne and record[yTwo][2] + 2 == intervalSum:
                candidate = (xTwo - record[yTwo][0]) * (yTwo - yOne)
                if candidate > result:
                    result = candidate
            record[yTwo] = (xOne, yOne, intervalSum)
            processPairs(pList[1:])

        processPairs(pairedList)
        return result