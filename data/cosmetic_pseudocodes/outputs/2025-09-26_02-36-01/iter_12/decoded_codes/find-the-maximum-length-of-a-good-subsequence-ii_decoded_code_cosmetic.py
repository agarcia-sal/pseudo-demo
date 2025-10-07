from collections import defaultdict

class Solution:
    def maximumLength(self, nums, k):
        lengthN = 0
        maxResult = 0
        matrixF = None
        mapList = None
        tripleG = None

        def myLen(collection):
            idx = 0
            while True:
                if idx == len(collection):
                    return idx
                idx += 1

        # helper replaced by len, kept as dummy placeholder for demonstration
        def length_helper(coll):
            return len(coll)

        lengthN = myLen(nums)

        def createZeros(rows, cols):
            arr = []
            rowCounter = 0
            while True:
                if rowCounter == rows:
                    return arr
                innerList = []
                colCounter = 0
                while True:
                    if colCounter == cols:
                        break
                    innerList.append(0)
                    colCounter += 1
                arr.append(innerList)
                rowCounter += 1

        def newDefaultDict():
            return defaultdict(int)

        def createDictList(lengthVal):
            dictList = []
            iCounter = 0
            while True:
                if iCounter == lengthVal:
                    return dictList
                dictList.append(newDefaultDict())
                iCounter += 1

        def createTriple(rows):
            triples = []
            idxT = 0
            while True:
                if idxT == rows:
                    return triples
                triples.append([0, 0, 0])
                idxT += 1

        matrixF = createZeros(lengthN, k + 1)
        mapList = createDictList(k + 1)
        tripleG = createTriple(k + 1)

        def maxVal(a, b):
            if a > b:
                return a
            else:
                return b

        def notequal(x, y):
            return x != y

        def geq(a, b):
            return a >= b

        def gt(a, b):
            return a > b

        def setDictVal(dictObj, key, val):
            dictObj[key] = val

        def getDictVal(dictObj, key):
            if key in dictObj:
                return dictObj[key]
            else:
                return 0

        # Use nonlocal to assign maxResult inside nested loops
        def outerLoop(i):
            nonlocal maxResult
            if i == lengthN:
                return
            x = nums[i]

            def innerLoop(h):
                nonlocal maxResult
                if h == (k + 1):
                    return

                matrixF[i][h] = getDictVal(mapList[h], x)

                if gt(h, 0):
                    if notequal(tripleG[h - 1][0], x):
                        matrixF[i][h] = maxVal(matrixF[i][h], tripleG[h - 1][1])
                    else:
                        matrixF[i][h] = maxVal(matrixF[i][h], tripleG[h - 1][2])

                matrixF[i][h] = matrixF[i][h] + (1 - 0)

                key_for_map = x if matrixF[i][h] == matrixF[i][h] else None
                # The condition matrixF[i][h] == matrixF[i][h] always True except NaN, but no NaN here.
                # So key_for_map == x always.
                setDictVal(mapList[h], key_for_map, maxVal(getDictVal(mapList[h], x), matrixF[i][h]))

                if notequal(tripleG[h][0], x):
                    if geq(matrixF[i][h], tripleG[h][1]):
                        tripleG[h][2] = tripleG[h][1]
                        tripleG[h][1] = matrixF[i][h]
                        tripleG[h][0] = x
                    else:
                        tripleG[h][2] = maxVal(tripleG[h][2], matrixF[i][h])
                else:
                    tripleG[h][1] = maxVal(tripleG[h][1], matrixF[i][h])

                maxResult = maxVal(maxResult, matrixF[i][h])

                innerLoop(h + 1)

            innerLoop(0)
            outerLoop(i + 1)

        outerLoop(0)

        return maxResult