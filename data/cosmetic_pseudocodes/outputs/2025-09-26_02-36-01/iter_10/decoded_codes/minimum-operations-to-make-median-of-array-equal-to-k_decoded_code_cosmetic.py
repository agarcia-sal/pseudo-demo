class Solution:
    def minOperationsToMakeMedianK(self, nums, k):
        def bubbleSortAscending(A):
            while True:
                passCheck = False
                for idxOuter in range(len(A) - 1):
                    if A[idxOuter] > A[idxOuter + 1]:
                        runnerTemp = A[idxOuter]
                        A[idxOuter] = A[idxOuter + 1]
                        A[idxOuter + 1] = runnerTemp
                        passCheck = True
                if not passCheck:
                    break

        def retrieveElement(B, pos):
            return B[pos]

        def absoluteDifference(x, y):
            if x > y:
                return x - y
            else:
                return y - x

        def incrementBy(refValue, inc):
            refValue = refValue + inc
            return refValue

        bubbleSortAscending(nums)
        countElements = len(nums)
        midSpot = countElements // 2

        if retrieveElement(nums, midSpot) == k:
            return 0

        actionCount = 0

        def checkLessThan(valA, valB):
            return valA < valB

        def checkGreaterThan(valA, valB):
            return valA > valB

        def checkGreaterEqual(valA, valB):
            return not (valA < valB)

        def checkLessEqual(valA, valB):
            return not (valA > valB)

        def isOutOfRange(index, upperLimit, lowerLimit):
            return (index >= upperLimit) or (index < lowerLimit)

        def addOperationIncrement(currentOps, targetVal, currentVal):
            return currentOps + absoluteDifference(targetVal, currentVal)

        def isAtUpperBoundary(pos, limit):
            return pos >= limit

        def isAtLowerBoundary(pos):
            return pos < 0

        if checkLessThan(retrieveElement(nums, midSpot), k):
            def recurForwardCheck(pos, maxPos, accumOps):
                if isAtUpperBoundary(pos, maxPos):
                    return accumOps
                if checkLessThan(retrieveElement(nums, pos), k):
                    accumOps = addOperationIncrement(accumOps, k, retrieveElement(nums, pos))
                    return recurForwardCheck(pos + 1, maxPos, accumOps)
                else:
                    return accumOps

            actionCount = recurForwardCheck(midSpot, countElements, actionCount)
        else:
            def recurBackwardCheck(pos, accumOps):
                if isAtLowerBoundary(pos):
                    return accumOps
                if checkGreaterThan(retrieveElement(nums, pos), k):
                    accumOps = addOperationIncrement(accumOps, retrieveElement(nums, pos), k)
                    return recurBackwardCheck(pos - 1, accumOps)
                else:
                    return accumOps

            actionCount = recurBackwardCheck(midSpot, actionCount)

        return actionCount