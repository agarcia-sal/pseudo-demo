from bisect import bisect_left

class Fenwick:
    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def add(self, index):
        while index < len(self.tree):
            self.tree[index] += 1
            increment = index & (-index)
            index += increment

    def pre(self, index):
        accumulator = 0
        while index > 0:
            accumulator += self.tree[index]
            index &= index - 1
        return accumulator

    def query(self, left, right):
        return self.pre(right) - self.pre(left - 1)


class Solution:
    def maxRectangleArea(self, xCoord, yCoord):
        combinedPairs = list(zip(xCoord, yCoord))
        combinedPairs.sort(key=lambda p: (p[0], p[1]))

        uniqueYs = sorted(set(yCoord))
        maximumArea = -1

        fenw = Fenwick(len(uniqueYs))
        startIndex = bisect_left(uniqueYs, combinedPairs[0][1]) + 1
        fenw.add(startIndex)
        history = {}

        i = 0
        while i < len(combinedPairs) - 1:
            pointA = combinedPairs[i]
            pointB = combinedPairs[i + 1]

            yPos = bisect_left(uniqueYs, pointB[1]) + 1
            fenw.add(yPos)

            if pointA[0] != pointB[0]:
                i += 1
                continue

            leftBound = bisect_left(uniqueYs, pointA[1]) + 1
            currentSum = fenw.query(leftBound, yPos)

            if (pointB[1] in history and
                history[pointB[1]][1] == pointA[1] and
                history[pointB[1]][2] + 2 == currentSum):
                candidateArea = (pointB[0] - history[pointB[1]][0]) * (pointB[1] - pointA[1])
                if candidateArea > maximumArea:
                    maximumArea = candidateArea

            history[pointB[1]] = (pointA[0], pointA[1], currentSum)
            i += 1

        return maximumArea