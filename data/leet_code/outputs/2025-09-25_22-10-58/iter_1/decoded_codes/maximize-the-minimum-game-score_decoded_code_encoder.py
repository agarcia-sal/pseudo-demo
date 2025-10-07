from math import ceil

class Solution:
    def maxScore(self, points, m):
        def isPossible(minVal, m):
            moves = 0
            prevMoves = 0
            for i, point in enumerate(points):
                required = ceil(minVal / point)
                diff = required - prevMoves
                if diff < 0:
                    required = 0
                else:
                    required = diff
                if required > 0:
                    moves += 2 * required - 1
                    prevMoves = required - 1
                elif i + 1 < len(points):
                    moves += 1
                    prevMoves = 0
                if moves > m:
                    return False
            return True

        l = 0
        r = ((m + 1) // 2) * (points[0] + 1)

        while l < r:
            mid = (l + r + 1) // 2
            if isPossible(mid, m):
                l = mid
            else:
                r = mid - 1

        return l