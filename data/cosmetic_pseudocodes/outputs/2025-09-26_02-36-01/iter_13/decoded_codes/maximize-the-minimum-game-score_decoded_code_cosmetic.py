import math
from typing import List

class Solution:
    def maxScore(self, points: List[int], m: int) -> int:
        def isPossible(minVal: int, m: int) -> bool:
            counter = 0
            prior = 0
            idx = 0
            n = len(points)
            while idx < n:
                curPoint = points[idx]
                neededRaw = (minVal + curPoint - 1) / curPoint
                neededFloor = math.floor(neededRaw)
                needed = neededFloor
                if (needed - prior) < 0:
                    needed = 0
                else:
                    needed = needed - prior

                if needed > 0:
                    counter += 2 * needed - 1
                    prior = needed - 1
                else:
                    if idx + 1 < n:
                        counter += 1
                        prior = 0
                if counter > m:
                    return False
                idx += 1
            return True

        low = 0
        high = ((m + 1) // 2) * (points[0] + 1)

        while low < high:
            midpoint = (low + high + 1) // 2
            if isPossible(midpoint, m):
                low = midpoint
            else:
                high = midpoint - 1

        return low