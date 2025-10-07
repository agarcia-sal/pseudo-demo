import math

class Solution:
    def maxScore(self, points, m):
        def isPossible(minVal, m):
            countMoves = 0
            prevCount = 0
            idx = 0
            n = len(points)
            while idx < n:
                currPoint = points[idx]
                calcReq = math.ceil((minVal + currPoint - 1) / currPoint)
                if (calcReq - prevCount) < 0:
                    calcReq = 0
                else:
                    calcReq = calcReq - prevCount
                if calcReq > 0:
                    countMoves += (calcReq * 2 - 1)
                    prevCount = calcReq - 1
                else:
                    if (idx + 1) < n:
                        countMoves += 1
                        prevCount = 0
                if countMoves > m:
                    return False
                idx += 1
            return True

        low = 0
        upperBound = (((m + 1) // 2) * points[0]) + 1
        high = upperBound

        while low < high:
            midPoint = (low + high + 1) // 2
            if isPossible(midPoint, m):
                low = midPoint
            else:
                high = midPoint - 1

        return low