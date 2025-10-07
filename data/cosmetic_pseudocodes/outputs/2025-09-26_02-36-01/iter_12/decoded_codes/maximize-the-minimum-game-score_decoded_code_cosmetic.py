class Solution:
    def maxScore(self, points, m):
        def canAchieve(target, limit):
            def ceilDiv(a, b):
                return (a + b - 1) // b

            totalSteps = 0
            prevReq = 0
            idx = 0
            lenPts = len(points)

            while idx < lenPts:
                currPt = points[idx]

                needed = ceilDiv(target + currPt - 1, currPt)
                diff = needed - prevReq
                needed = diff if diff >= 0 else 0

                if needed > 0:
                    totalSteps += (needed * 2) - 1
                    prevReq = needed - 1
                else:
                    if idx + 1 < lenPts:
                        totalSteps += 1
                        prevReq = 0

                if totalSteps > limit:
                    return False
                idx += 1
            return True

        leftBound = 0
        rightBound = (((m + 1) // 2) * points[0]) + 1
        answer = 0

        while leftBound < rightBound:
            midVal = (leftBound + rightBound + 1) // 2
            if canAchieve(midVal, m):
                leftBound = midVal
                answer = leftBound
            else:
                rightBound = midVal - 1

        return answer