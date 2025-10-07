from typing import List

class Solution:
    def maxScore(self, points: List[int], m: int) -> int:
        def isPossible(minVal: int, m: int) -> bool:
            totalMoves = 0
            lastReq = 0

            def ceilingDiv(a: int, b: int) -> int:
                # Integer ceiling division for positive integers
                return (a + b - 1) // b

            def greaterThan(a: int, b: int) -> bool:
                return a > b

            def lessThan(a: int, b: int) -> bool:
                return a < b

            def loopRecursive(idx: int):
                nonlocal totalMoves, lastReq
                if idx >= len(points):
                    return

                currentPoint = points[idx]
                needed = ceilingDiv(minVal + currentPoint - 1, currentPoint)

                adjusted = max(0, needed - lastReq)

                if greaterThan(adjusted, 0):
                    addedMoves = 2 * adjusted - 1
                    totalMoves += addedMoves
                    lastReq = adjusted - 1
                else:
                    if lessThan(idx + 1, len(points)):
                        totalMoves += 1
                        lastReq = 0

                if greaterThan(totalMoves, m):
                    return
                loopRecursive(idx + 1)

            loopRecursive(0)

            return totalMoves <= m

        lowerBound = 0
        # The upper bound is ((m + 1)/2) * (points[0] + 1), following integer division logic
        upperBound = ((m + 1) // 2) * (points[0] + 1)

        def binarySearch(low: int, high: int) -> int:
            result = low

            def bsHelper(lc: int, rc: int):
                nonlocal result
                if lc >= rc:
                    return
                middle = (lc + rc + 1) // 2
                if isPossible(middle, m):
                    result = middle
                    bsHelper(middle, rc)
                else:
                    bsHelper(lc, middle - 1)

            bsHelper(low, high)
            return result

        return binarySearch(lowerBound, upperBound)