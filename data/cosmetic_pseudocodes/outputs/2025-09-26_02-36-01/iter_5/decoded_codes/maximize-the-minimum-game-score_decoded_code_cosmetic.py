class Solution:
    def maxScore(self, points, m):
        n = len(points)

        def isPossible(threshold, limit):
            totalMoves = 0
            previousCount = 0

            def recurse(idx):
                nonlocal totalMoves, previousCount
                if idx == n:
                    return True

                currentPoint = points[idx]
                neededRaw = (threshold + currentPoint - 1) // currentPoint
                neededAdjusted = 0
                if neededRaw - previousCount >= 0:
                    neededAdjusted = neededRaw - previousCount

                if neededAdjusted > 0:
                    totalMoves += 2 * neededAdjusted - 1
                    previousCount = neededAdjusted - 1
                elif idx + 1 < n:
                    totalMoves += 1
                    previousCount = 0

                if totalMoves > limit:
                    return False

                return recurse(idx + 1)

            return recurse(0)

        leftBound = 0
        rightBound = ((m + 1) // 2) * points[0] + 1

        while leftBound < rightBound:
            midPoint = (leftBound + rightBound + 1) // 2
            if isPossible(midPoint, m):
                leftBound = midPoint
            else:
                rightBound = midPoint - 1

        return leftBound