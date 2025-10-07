from bisect import bisect_left

class Fenwick:
    def __init__(self, n):
        self.tree = [0] * (n + 1)

    def add(self, i):
        while i < len(self.tree):
            self.tree[i] += 1
            i += i & (-i)

    def pre(self, i):
        total = 0
        while i > 0:
            total += self.tree[i]
            i &= i - 1
        return total

    def query(self, l, r):
        return self.pre(r) - self.pre(l - 1)

class Solution:
    def maxRectangleArea(self, xCoord, yCoord):
        combined = list(zip(xCoord, yCoord))
        combined.sort()
        uniqueYs = sorted(set(yCoord))
        maximumArea = -1
        fenwTree = Fenwick(len(uniqueYs))
        fenwTree.add(bisect_left(uniqueYs, combined[0][1]) + 1)
        records = {}

        def processPairs(index):
            if index == len(combined) - 1:
                return
            px1, py1 = combined[index]
            px2, py2 = combined[index + 1]
            yIndex = bisect_left(uniqueYs, py2) + 1
            fenwTree.add(yIndex)
            if px1 != px2:
                processPairs(index + 1)
                return
            currentSum = fenwTree.query(bisect_left(uniqueYs, py1) + 1, yIndex)
            if (py2 in records and records[py2][1] == py1 and (records[py2][2] + 2) == currentSum):
                areaCandidate = (px2 - records[py2][0]) * (py2 - py1)
                if areaCandidate > maximumArea:
                    nonlocal maximumArea
                    maximumArea = areaCandidate
            records[py2] = (px1, py1, currentSum)
            processPairs(index + 1)

        processPairs(0)
        return maximumArea