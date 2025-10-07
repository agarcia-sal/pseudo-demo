from bisect import bisect_left

class Fenwick:
    def __init__(self, n):
        lengthAugmented = n + 1
        self.tree = [0] * lengthAugmented

    def add(self, i):
        while i < len(self.tree):
            self.tree[i] += 1
            delta = i & (-i)
            i += delta

    def pre(self, i):
        accumulator = 0
        while i > 0:
            accumulator += self.tree[i]
            i &= (i - 1)
        return accumulator

    def query(self, l, r):
        rightSum = self.pre(r)
        leftSum = self.pre(l - 1)
        return rightSum - leftSum


class Solution:
    def maxRectangleArea(self, xCoord, yCoord):
        combinedPoints = []
        indexCounter = 0
        while indexCounter < len(xCoord):
            xElement = xCoord[indexCounter]
            yElement = yCoord[indexCounter]
            combinedPoints.append((xElement, yElement))
            indexCounter += 1

        combinedPoints.sort(key=lambda p: (p[0], p[1]))

        uniqueYsTemp = []
        seenYs = set()
        pointer = 0
        while pointer < len(yCoord):
            elem = yCoord[pointer]
            if elem not in seenYs:
                seenYs.add(elem)
                uniqueYsTemp.append(elem)
            pointer += 1

        uniqueYsTemp.sort()
        uniqueYs = uniqueYsTemp

        answer_best_so_far = -1
        fenwickTree = Fenwick(len(uniqueYs))
        firstYIndex = bisect_left(uniqueYs, combinedPoints[0][1]) + 1
        fenwickTree.add(firstYIndex)

        previousMap = {}
        pos1 = 0
        pos2 = 1
        while pos2 < len(combinedPoints):
            xVal1, yVal1 = combinedPoints[pos1]
            xVal2, yVal2 = combinedPoints[pos2]
            mappedY2 = bisect_left(uniqueYs, yVal2) + 1
            fenwickTree.add(mappedY2)

            if xVal1 != xVal2:
                pos1 = pos2
                pos2 += 1
                continue

            mappedY1 = bisect_left(uniqueYs, yVal1) + 1
            currentQuery = fenwickTree.query(mappedY1, mappedY2)

            if yVal2 in previousMap and previousMap[yVal2][1] == yVal1 and previousMap[yVal2][2] + 2 == currentQuery:
                candidateArea = (xVal2 - previousMap[yVal2][0]) * (yVal2 - yVal1)
                if candidateArea > answer_best_so_far:
                    answer_best_so_far = candidateArea

            previousMap[yVal2] = (xVal1, yVal1, currentQuery)
            pos1 = pos2
            pos2 += 1

        return answer_best_so_far