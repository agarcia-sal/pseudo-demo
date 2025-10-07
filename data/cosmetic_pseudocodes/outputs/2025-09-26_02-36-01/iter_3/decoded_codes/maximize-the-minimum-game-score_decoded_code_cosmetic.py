import math

class Solution:
    def maxScore(self, points, m):
        def isPossible(minVal, m):
            totalMoves = 0
            prevStepCount = 0
            idx = 0
            n = len(points)
            while idx < n:
                currentPoint = points[idx]
                needed = math.ceil((minVal + currentPoint - 1) / currentPoint)
                if needed - prevStepCount < 0:
                    needed = 0
                else:
                    needed = needed - prevStepCount
                if needed > 0:
                    totalMoves += 2 * needed - 1
                    prevStepCount = needed - 1
                elif idx + 1 < n:
                    totalMoves += 1
                    prevStepCount = 0
                if totalMoves > m:
                    return False
                idx += 1
            return True

        leftBoundary = 0
        rightBoundary = (m + 1) // 2 * (points[0] + 1)

        while leftBoundary < rightBoundary:
            middle = (leftBoundary + rightBoundary + 1) // 2
            if isPossible(middle, m):
                leftBoundary = middle
            else:
                rightBoundary = middle - 1

        return leftBoundary