import math

class Solution:
    def maxScore(self, points, m):
        def isPossible(valMin, m):
            totalMoves = 0
            priorMoves = 0
            pos = 0
            length = len(points)
            while pos < length:
                currPoint = points[pos]
                calcReq = math.ceil((valMin + currPoint - 1) / currPoint)
                if (calcReq - priorMoves) < 0:
                    calcReq = 0
                else:
                    calcReq = calcReq - priorMoves

                if calcReq > 0:
                    totalMoves += (calcReq * 2 - 1)
                    priorMoves = calcReq - 1
                elif (pos + 1) < length:
                    totalMoves += 1
                    priorMoves = 0

                if totalMoves > m:
                    return False
                pos += 1
            return True

        low = 0
        high = ((m + 1) // 2) * (points[0] + 1)

        while low < high:
            middle = (low + high + 1) // 2
            if isPossible(middle, m):
                low = middle
            else:
                high = middle - 1

        return low