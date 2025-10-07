from collections import defaultdict

class Solution:
    def maximumLength(self, psi, phi):
        def initMatrix(rowCount, colCount):
            lib = []
            count1 = 0
            while count1 < rowCount:
                tempRow = []
                count2 = 0
                while count2 < colCount:
                    tempRow.append(0)
                    count2 += 1
                lib.append(tempRow)
                count1 += 1
            return lib

        def initListOfDicts(lengthVal):
            outerList = []
            idx = 0
            while idx < lengthVal:
                outerList.append(defaultdict(int))
                idx += 1
            return outerList

        def maxOfTwo(p, q):
            return p if p > q else q

        def updateG(arr, ind, val, keyVal):
            if arr[ind][0] != keyVal:
                if val >= arr[ind][1]:
                    arr[ind][2] = arr[ind][1]
                    arr[ind][1] = val
                    arr[ind][0] = keyVal
                else:
                    arr[ind][2] = maxOfTwo(arr[ind][2], val)
            else:
                arr[ind][1] = maxOfTwo(arr[ind][1], val)

        m = len(psi)
        q = phi + 1
        fMatrix = initMatrix(m, q)
        mpList = initListOfDicts(q)
        gMatrix = initMatrix(q, 3)

        ultimateAns = 0

        def outerLoopCounter(indOuter):
            if indOuter >= m:
                return

            currentValue = psi[indOuter]
            innerIndex = 0

            def innerLoopCounter(indInner):
                nonlocal ultimateAns
                if indInner > phi:
                    outerLoopCounter(indOuter + 1)
                    return

                fMatrix[indOuter][indInner] = mpList[indInner].get(currentValue, 0)

                if indInner > 0:
                    if gMatrix[indInner - 1][0] != currentValue:
                        fMatrix[indOuter][indInner] = maxOfTwo(fMatrix[indOuter][indInner], gMatrix[indInner - 1][1])
                    else:
                        fMatrix[indOuter][indInner] = maxOfTwo(fMatrix[indOuter][indInner], gMatrix[indInner - 1][2])

                fMatrix[indOuter][indInner] += 1

                mpList[indInner][currentValue] = maxOfTwo(mpList[indInner].get(currentValue, 0), fMatrix[indOuter][indInner])

                updateG(gMatrix, indInner, fMatrix[indOuter][indInner], currentValue)

                ultimateAns = maxOfTwo(ultimateAns, fMatrix[indOuter][indInner])

                innerLoopCounter(indInner + 1)

            innerLoopCounter(0)

        outerLoopCounter(0)

        return ultimateAns