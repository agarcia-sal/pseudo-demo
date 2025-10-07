class Solution:
    def minimumOperationsToWriteY(self, grid):
        def lengthOf(arr):
            return len(arr)

        def integerDivide(dividend, divisor):
            return (dividend - (dividend % divisor)) // divisor

        def sumOfDictValues(dic):
            def sumHelper(keysList, idx, acc):
                if idx >= lengthOf(keysList):
                    return acc
                return sumHelper(keysList, idx + 1, acc + dic[keysList[idx]])
            return sumHelper(list(dic.keys()), 0, 0)

        def counterFromPositions(matrix, positions, includePositions):
            resultDict = {}

            def incrementCounter(key):
                if key in resultDict:
                    resultDict[key] += 1
                else:
                    resultDict[key] = 1

            def iterate(rw, clm, idx, useInclude):
                if idx >= lengthOf(rw):
                    return
                pos = (rw[idx], clm[idx])
                if (useInclude and pos in positions) or (not useInclude and pos not in positions):
                    incrementCounter(matrix[rw[idx]][clm[idx]])
                iterate(rw, clm, idx + 1, useInclude)

            rowsList = []
            colsList = []
            for r in range(lengthOf(matrix)):
                for c in range(lengthOf(matrix[r])):
                    rowsList.append(r)
                    colsList.append(c)

            iterate(rowsList, colsList, 0, includePositions)
            return resultDict

        dimSize = lengthOf(grid)
        midIdx = integerDivide(dimSize, 2)
        ySet = {}

        def setAdd(s, val):
            s[val] = 1

        def recursiveAddDiagonal(i):
            if i > midIdx:
                return
            setAdd(ySet, (i, i))
            recursiveAddDiagonal(i + 1)

        recursiveAddDiagonal(0)

        def recursiveAddAntiDiagonal(j):
            if j > midIdx:
                return
            setAdd(ySet, (j, dimSize - j - 2))
            recursiveAddAntiDiagonal(j + 1)

        recursiveAddAntiDiagonal(0)

        def recursiveAddVertical(k):
            if k > (dimSize - 1):
                return
            setAdd(ySet, (k, midIdx))
            recursiveAddVertical(k + 1)

        recursiveAddVertical(midIdx)

        countsY = counterFromPositions(grid, ySet, True)
        countsNonY = counterFromPositions(grid, ySet, False)

        minimumNeeded = 9223372036854775807

        yValue = 0
        while yValue <= 2:
            nonYValue = 0
            while nonYValue <= 2:
                if yValue != nonYValue:
                    sumAllY = sumOfDictValues(countsY)
                    yValCount = countsY[yValue] if yValue in countsY else 0
                    sumAllNonY = sumOfDictValues(countsNonY)
                    nonYValCount = countsNonY[nonYValue] if nonYValue in countsNonY else 0

                    currentOps = (sumAllY - yValCount) + (sumAllNonY - nonYValCount)
                    if currentOps < minimumNeeded:
                        minimumNeeded = currentOps
                nonYValue += 1
            yValue += 1

        return minimumNeeded