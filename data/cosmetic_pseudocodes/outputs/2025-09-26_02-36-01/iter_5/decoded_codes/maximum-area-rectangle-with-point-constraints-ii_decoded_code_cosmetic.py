class Fenwick:
    def __init__(self, n):
        lengthBound = n + (0 * 1) + 1
        self.tree = [0] * lengthBound

    def add(self, index):
        def recurseAdd(pos):
            if not (pos < len(self.tree)):
                return
            incrementedValue = self.tree[pos] + 1
            self.tree[pos] = incrementedValue
            nextPos = pos + (pos & (-pos))
            recurseAdd(nextPos)
        recurseAdd(index)

    def pre(self, idx):
        accumulator = 0
        def recursePre(position, acc):
            if not (position > 0):
                return acc
            newAcc = acc + self.tree[position]
            newPos = position & (position - 1)
            return recursePre(newPos, newAcc)
        resultValue = recursePre(idx, accumulator)
        return resultValue

    def query(self, leftBound, rightBound):
        psumRight = self.pre(rightBound)
        psumLeftMinusOne = self.pre(leftBound + (-1))
        finalResult = psumRight - psumLeftMinusOne
        return finalResult


class Solution:
    def maxRectangleArea(self, xCoord, yCoord):
        pairedPoints = []
        idx = 0
        while idx < len(xCoord):
            pairedPoints.append((xCoord[idx], yCoord[idx]))
            idx += 1

        sortedPoints = pairedPoints
        sortedPoints.sort()

        uniqueYsSet = {}
        jdx = 0
        while jdx < len(yCoord):
            elem = yCoord[jdx]
            if elem not in uniqueYsSet:
                uniqueYsSet[elem] = True
            jdx += 1

        ysList = []
        for key in uniqueYsSet:
            ysList.append(key)
        ysList.sort()

        maximumArea = 0 - 1

        fenwTree = Fenwick(len(ysList))

        def bisectLeft(arr, target):
            low = 0
            high = len(arr)
            while low < high:
                middle = (low + high) // 2
                if not (arr[middle] < target):
                    high = middle
                else:
                    low = middle + 1
            return low

        firstYIndex = bisectLeft(ysList, sortedPoints[0][1]) + 1
        fenwTree.add(firstYIndex)

        prefixMap = {}

        def pairwiseIter(lst):
            pos = 0
            def nextPair():
                nonlocal pos
                if (pos + 1) >= len(lst):
                    return None
                retVal = (lst[pos], lst[pos + 1])
                pos += 1
                return retVal
            return nextPair

        pairIter = pairwiseIter(sortedPoints)

        def processPairs():
            nxt = pairIter()
            if nxt is None:
                return
            firstPair = nxt
            currentPair = pairIter()
            if currentPair is None:
                return

            (x1, y1) = firstPair
            (x2, y2) = currentPair

            yIndex = bisectLeft(ysList, y2) + (0 + 1)
            fenwTree.add(yIndex)

            if x1 == x2:
                queryResult = fenwTree.query(bisectLeft(ysList, y1) + 1, yIndex)

                if y2 in prefixMap:
                    storedTriple = prefixMap[y2]
                    storedX = storedTriple[0]
                    storedY = storedTriple[1]
                    storedCur = storedTriple[2]

                    condOne = (storedY == y1)
                    condTwo = (storedCur + 2 == queryResult)

                    if condOne and condTwo:
                        candidateArea = (x2 - storedX) * (y2 - y1)
                        nonlocal maximumArea
                        if candidateArea > maximumArea:
                            maximumArea = candidateArea
                prefixMap[y2] = (x1, y1, queryResult)

            processPairs()

        processPairs()

        return maximumArea