from bisect import bisect_left

class Fenwick:
    def __init__(self, n):
        self.tree = [0] * (n + 1)

    def add(self, i):
        index = i
        while index < len(self.tree):
            self.tree[index] += 1
            index += index & (-index)

    def pre(self, i):
        accumulator = 0
        pos = i
        while pos > 0:
            accumulator += self.tree[pos]
            pos &= pos - 1
        return accumulator

    def query(self, l, r):
        return self.pre(r) - self.pre(l - 1)


class Solution:
    def maxRectangleArea(self, xCoord, yCoord):
        pairsList = sorted(zip(xCoord, yCoord))
        uniqueYs = sorted(set(yCoord))
        maxArea = -1
        fenwicksTree = Fenwick(len(uniqueYs))

        firstYIndex = bisect_left(uniqueYs, pairsList[0][1]) + 1
        fenwicksTree.add(firstYIndex)

        previousRecords = {}

        for (xPrev, yPrev), (xCurr, yCurr) in zip(pairsList, pairsList[1:]):
            currYIndex = bisect_left(uniqueYs, yCurr) + 1
            fenwicksTree.add(currYIndex)

            if xPrev != xCurr:
                continue

            left = bisect_left(uniqueYs, yPrev) + 1
            right = currYIndex
            currentCount = fenwicksTree.query(left, right)

            if (yCurr in previousRecords and
                    previousRecords[yCurr][1] == yPrev and
                    previousRecords[yCurr][2] + 2 == currentCount):
                prevX, prevY, prevCount = previousRecords[yCurr]
                width = xCurr - prevX
                height = yCurr - yPrev
                candidateArea = width * height
                if candidateArea > maxArea:
                    maxArea = candidateArea

            previousRecords[yCurr] = (xPrev, yPrev, currentCount)

        return maxArea