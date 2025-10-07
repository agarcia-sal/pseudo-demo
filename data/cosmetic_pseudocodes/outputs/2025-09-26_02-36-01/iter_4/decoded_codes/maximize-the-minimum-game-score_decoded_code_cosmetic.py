class Solution:
    def maxScore(self, points, m):
        def isPossible(minVal, m):
            totalMoves = 0
            prevUsed = 0
            idx = 0
            n = len(points)
            while idx < n:
                pt = points[idx]
                divCalc = (minVal + pt - 1) // pt
                req = divCalc
                if (req - prevUsed) < 0:
                    req = 0
                else:
                    req = req - prevUsed
                if req > 0:
                    totalMoves += 2 * req - 1
                    prevUsed = req - 1
                elif idx + 1 < n:
                    totalMoves += 1
                    prevUsed = 0
                if totalMoves > m:
                    return False
                idx += 1
            return True

        leftBound = 0
        rightBound = ((m + 1) // 2) * (points[0] + 1)

        while leftBound < rightBound:
            middleVal = (leftBound + rightBound + 1) // 2
            if isPossible(middleVal, m):
                leftBound = middleVal
            else:
                rightBound = middleVal - 1

        return leftBound