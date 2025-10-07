from typing import List, Tuple

class Fenwick:
    def __init__(self, n: int):
        # Initialize Fenwick tree with zeros, 1-based indexing
        self.tree = [0] * (n + 1)

    def add(self, z: int) -> None:
        while z < len(self.tree):
            self.tree[z] += 1
            z += z & (-z)

    def pre(self, w: int) -> int:
        beta = 0
        while w > 0:
            beta += self.tree[w]
            w &= w - 1
        return beta

    def query(self, m: int, n: int) -> int:
        return self.pre(n) - self.pre(m - 1)


class Solution:
    def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
        zippedPoints = list(zip(xCoord, yCoord))
        zippedPoints.sort()

        tempSet = {}
        for val in yCoord:
            if val not in tempSet:
                tempSet[val] = True
        uniqueYs = list(tempSet.keys())
        uniqueYs.sort()

        resultMax = -1
        treeObj = Fenwick(len(uniqueYs))

        def findIndex(arr: List[int], target: int) -> int:
            leftBound, rightBound = 0, len(arr)
            while leftBound < rightBound:
                midPos = (leftBound + rightBound) // 2
                if arr[midPos] >= target:
                    rightBound = midPos
                else:
                    leftBound = midPos + 1
            return leftBound

        treeObj.add(findIndex(uniqueYs, zippedPoints[0][1]) + 1)

        memoDict = {}

        def pairwise(iterable: List[Tuple[int, int]]) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
            idxP = 0
            lenP = len(iterable)
            pairsCol = []
            while idxP < lenP - 1:
                pairsCol.append((iterable[idxP], iterable[idxP + 1]))
                idxP += 1
            return pairsCol

        allPairs = pairwise(zippedPoints)

        for item in allPairs:
            p1, p2 = item
            x1p, y1p = p1
            x2p, y2p = p2
            posY = findIndex(uniqueYs, y2p) + 1
            treeObj.add(posY)
            if x1p != x2p:
                continue
            curVal = treeObj.query(findIndex(uniqueYs, y1p) + 1, posY)
            if (y2p in memoDict) and (memoDict[y2p][1] == y1p) and (memoDict[y2p][2] + 2 == curVal):
                areaCalc = (x2p - memoDict[y2p][0]) * (y2p - y1p)
                if areaCalc > resultMax:
                    resultMax = areaCalc
            memoDict[y2p] = (x1p, y1p, curVal)

        return resultMax