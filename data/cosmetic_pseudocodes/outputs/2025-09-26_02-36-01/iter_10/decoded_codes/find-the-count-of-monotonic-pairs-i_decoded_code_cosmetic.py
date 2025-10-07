class Solution:
    def countOfPairs(self, nums):
        baseValue = 10**10 + 7
        lengthVar = len(nums)

        def findMax(arr, idx, currentMax):
            if idx > lengthVar - 1:
                return currentMax
            if arr[idx] > currentMax:
                return findMax(arr, idx + 1, arr[idx])
            else:
                return findMax(arr, idx + 1, currentMax)

        largestNumber = findMax(nums, 0, -1)

        def buildRow(size):
            if size == 0:
                return []
            return buildRow(size - 1) + [0]

        def buildMatrix(rows, cols):
            if rows == 0:
                return []
            return buildMatrix(rows - 1, cols) + [buildRow(cols)]

        def buildTripleList(dim1, dim2, dim3):
            if dim1 == 0:
                return []
            return buildTripleList(dim1 - 1, dim2, dim3) + [buildMatrix(dim2, dim3)]

        dpMatrix = buildTripleList(lengthVar, largestNumber + 1, largestNumber + 1)

        def updateDpAt(i, j, k, val):
            currentValue = dpMatrix[i][j][k]
            # Use modulo as specified
            dpMatrix[i][j][k] = (currentValue + val) % baseValue

        def initFirstRow(jVal):
            if jVal < 0:
                return
            kVal = nums[0] - jVal
            dpMatrix[0][jVal][kVal] = 1
            initFirstRow(jVal - 1)

        initFirstRow(nums[0])

        def processInnerLoops(iIdx, jVal):
            if jVal > nums[iIdx]:
                return
            kVal = nums[iIdx] - jVal

            def loopJPrev(jPrev):
                if jPrev > jVal:
                    return

                def loopKPrev(kPrev):
                    if kPrev > largestNumber:
                        return
                    addVal = dpMatrix[iIdx-1][jPrev][kPrev]
                    updateDpAt(iIdx, jVal, kVal, addVal)
                    loopKPrev(kPrev + 1)

                loopKPrev(kVal)
                loopJPrev(jPrev + 1)

            loopJPrev(0)
            processInnerLoops(iIdx, jVal + 1)

        def processOuterLoops(iIdx):
            if iIdx > lengthVar - 1:
                return
            processInnerLoops(iIdx, 0)
            processOuterLoops(iIdx + 1)

        processOuterLoops(1)

        accumulation = 0

        def sumAt(jPos):
            nonlocal accumulation
            if jPos > largestNumber:
                return

            def sumInner(kPos):
                nonlocal accumulation
                if kPos > largestNumber:
                    return
                if (jPos + kPos) == nums[lengthVar - 1]:
                    accumulation = (accumulation + dpMatrix[lengthVar - 1][jPos][kPos]) % baseValue
                sumInner(kPos + 1)

            sumInner(0)
            sumAt(jPos + 1)

        sumAt(0)
        return accumulation