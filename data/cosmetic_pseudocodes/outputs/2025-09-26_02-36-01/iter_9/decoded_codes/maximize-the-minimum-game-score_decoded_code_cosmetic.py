class Solution:
    def maxScore(self, originList, limit):
        def ceil_divide(a, b):
            return (a + b - 1) // b

        def checkFeasibility(threshold, capacity):
            stepCount = 0
            backupCount = 0
            idx = 0
            n = len(originList)

            while idx < n:
                currentPoint = originList[idx]
                calcReq = ceil_divide(threshold + currentPoint - 1, currentPoint)

                adjustedReq = calcReq - backupCount
                if adjustedReq < 0:
                    adjustedReq = 0

                if adjustedReq > 0:
                    stepCount += 2 * adjustedReq - 1
                    backupCount = adjustedReq - 1
                else:
                    if idx + 1 < n:
                        stepCount += 1
                        backupCount = 0

                if stepCount > capacity:
                    return False

                idx += 1

            return True

        lowerBound = 0
        upperBound = ((limit + 1) // 2) * (originList[0] + 1)

        while lowerBound < upperBound:
            pivot = (lowerBound + upperBound + 1) // 2
            if checkFeasibility(pivot, limit):
                lowerBound = pivot
            else:
                upperBound = pivot - 1

        return lowerBound