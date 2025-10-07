from math import inf
from itertools import combinations

class Solution:
    def minimumSum(self, grid):
        positions = []
        rowCount = 0
        rowLimit = len(grid) - 1
        while rowCount < rowLimit:
            colCount = 0
            colLimit = len(grid[rowCount]) - 1
            while colCount < colLimit:
                if grid[rowCount] == 1 and grid[rowCount][colCount] == 1:
                    tmpPair = (rowCount, colCount)
                    positions.append(tmpPair)
                colCount += 1
            rowCount += 1

        def rect_area(points):
            if not points:
                result = 0
            else:
                firstIndices = []
                secondIndices = []
                idx = 0
                while idx < len(points):
                    firstIndices.append(points[idx][0])
                    secondIndices.append(points[idx][1])
                    idx += 1

                minFirst = firstIndices[0]
                maxFirst = firstIndices[0]
                indexF = 1
                while indexF < len(firstIndices):
                    if firstIndices[indexF] < minFirst:
                        minFirst = firstIndices[indexF]
                    if firstIndices[indexF] > maxFirst:
                        maxFirst = firstIndices[indexF]
                    indexF += 1

                minSecond = secondIndices[0]
                maxSecond = secondIndices[0]
                indexS = 1
                while indexS < len(secondIndices):
                    if secondIndices[indexS] < minSecond:
                        minSecond = secondIndices[indexS]
                    if secondIndices[indexS] > maxSecond:
                        maxSecond = secondIndices[indexS]
                    indexS += 1

                widthVal = (maxFirst - minFirst) + 1
                heightVal = (maxSecond - minSecond) + 1
                result = widthVal * heightVal
            return result

        minimalSum = inf
        total_ONES = len(positions)

        def iterate_i(i):
            if i >= total_ONES:
                return

            def iterate_j(j):
                if j >= total_ONES:
                    return

                def iterate_k(k):
                    if k >= (total_ONES + 1):
                        return

                    for firstComb in combinations(positions, i):
                        setPositions = set(positions)
                        setFirstComb = set(firstComb)
                        leftoverAfterFirst = setPositions - setFirstComb
                        needed_second = j - i
                        if needed_second < 0 or needed_second > len(leftoverAfterFirst):
                            continue
                        for secondComb in combinations(list(leftoverAfterFirst), needed_second):
                            setSecondComb = set(secondComb)
                            thirdComb = leftoverAfterFirst - setSecondComb
                            areaFirst = rect_area(firstComb)
                            areaSecond = rect_area(secondComb)
                            areaThird = rect_area(list(thirdComb))
                            if areaFirst > 0 and areaSecond > 0 and areaThird > 0:
                                sumAreas = areaFirst + areaSecond + areaThird
                                if sumAreas < minimalSum:
                                    nonlocal minimalSum
                                    minimalSum = sumAreas

                    iterate_k(k + 1)

                iterate_k(j + 1)
                iterate_j(j + 1)

            iterate_j(i + 1)
            iterate_i(i + 1)

        iterate_i(1)
        return minimalSum