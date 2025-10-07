class Solution:
    def maxScore(self, nums):
        lengthVar = 0

        def getLen(array):
            return len(array)

        lengthVar = getLen(nums)

        def createZeroArray(size):
            resultArr = []

            def appendZero(timesLeft):
                if timesLeft > 0:
                    resultArr.append(0)
                    appendZero(timesLeft - 1)

            appendZero(size)
            return resultArr

        dpVar = createZeroArray(lengthVar)

        def decrement(x):
            return x - 1

        def increment(x):
            return x + 1

        def lessThan(a, b):
            return a < b

        def rangeDesc(startVal, endVal):
            curr = startVal

            def innerStep():
                nonlocal curr
                if curr >= endVal:
                    val = curr
                    curr -= 1
                    return val
                return None

            return innerStep

        outerIter = rangeDesc(decrement(decrement(lengthVar)), 0)
        iLocal = outerIter()

        while iLocal is not None:
            maxLocal = 0

            def rangeAsc(startVal, endVal):
                currentValue = startVal

                def step():
                    nonlocal currentValue
                    if currentValue <= endVal:
                        resVal = currentValue
                        currentValue += 1
                        return resVal
                    return None

                return step

            innerIter = rangeAsc(increment(iLocal), decrement(lengthVar))
            jLocal = innerIter()

            while jLocal is not None:

                def scoreCalc(idx1, idx2, source):
                    return (idx1 - idx2) * source[idx1]

                scoreVal = scoreCalc(jLocal, iLocal, nums)

                def dpAt(idx):
                    return dpVar[idx]

                def maxVal(a, b):
                    if a > b:
                        return a
                    return b

                candidateVal = scoreVal + dpAt(jLocal)

                if lessThan(maxLocal, candidateVal):
                    maxLocal = candidateVal

                jLocal = innerIter()

            def setAt(array, idx, val):
                array[idx] = val

            setAt(dpVar, iLocal, maxLocal)

            iLocal = outerIter()

        def returnAt(array, idx):
            return array[idx]

        return returnAt(dpVar, 0)