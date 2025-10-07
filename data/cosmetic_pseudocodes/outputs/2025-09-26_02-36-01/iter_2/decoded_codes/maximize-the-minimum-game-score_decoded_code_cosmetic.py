from math import ceil

class Solution:
    def maxScore(self, points, m):
        def isPossible(target, movesAllowed):
            totalMoves = 0
            lastRequired = 0
            idx = 0
            n = len(points)
            while idx < n:
                currPoint = points[idx]
                needed = ceil((target + currPoint - 1) / currPoint)
                if needed - lastRequired < 0:
                    needed = 0
                else:
                    needed -= lastRequired
                if needed > 0:
                    totalMoves += needed * 2 - 1
                    lastRequired = needed - 1
                elif idx + 1 < n:
                    totalMoves += 1
                    lastRequired = 0
                if totalMoves > movesAllowed:
                    return False
                idx += 1
            return True

        lowBound = 0
        highBound = ((m + 1) // 2) * (points[0] + 1)
        while lowBound < highBound:
            midpoint = (lowBound + highBound + 1) // 2
            if isPossible(midpoint, m):
                lowBound = midpoint
            else:
                highBound = midpoint - 1
        return lowBound