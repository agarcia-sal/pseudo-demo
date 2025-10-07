from math import ceil

class Solution:
    def maxScore(self, points, m):
        def isPossible(minVal, m):
            usedMoves = 0
            leftover = 0
            n = len(points)
            for i in range(n):
                point = points[i]
                needed = ceil(minVal / point)
                diff = needed - leftover
                if diff < 0:
                    diff = 0
                if diff > 0:
                    usedMoves += 2 * diff - 1
                    leftover = diff - 1
                elif i < n - 1:
                    usedMoves += 1
                    leftover = 0
                if usedMoves > m:
                    return False
            return True

        left = 0
        right = ((m + 1) // 2) * (points[0] + 1)

        while left < right:
            middle = (left + right + 1) // 2
            if isPossible(middle, m):
                left = middle
            else:
                right = middle - 1
        return left