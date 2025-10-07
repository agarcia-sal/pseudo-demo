from math import inf
from functools import lru_cache

class Solution:
    def maxCollectedFruits(self, fruits):
        lengthVar = len(fruits)

        directionsAlpha = [(1, 1), (1, 0), (0, 1)]
        directionsBeta = [(1, -1), (1, 0), (1, 1)]
        directionsGamma = [(-1, 1), (0, 1), (1, 1)]

        @lru_cache(None)
        def recur(a1, b1, a2, b2, a3, b3):
            # Check boundary conditions
            if not (0 <= a1 < lengthVar and 0 <= b1 < lengthVar and
                    0 <= a2 < lengthVar and 0 <= b2 < lengthVar and
                    0 <= a3 < lengthVar and 0 <= b3 < lengthVar):
                return -inf

            # Check if all positions reached bottom-right corner
            if a1 == b1 == a2 == b2 == a3 == b3 == lengthVar - 1:
                return fruits[lengthVar - 1][lengthVar - 1]

            gatherCount = fruits[a1][b1]

            # If positions overlap between A1 and A2 or A1 and A3, avoid double counting for a1,b1
            if (a1 == a2 and b1 == b2) or (a1 == a3 and b1 == b3):
                gatherCount = 0

            # Add fruit counts for positions (a2,b2) and (a3,b3), carefully avoid counting twice if equal
            if a2 == a3 and b2 == b3:
                gatherCount += fruits[a2][b2]
            else:
                gatherCount += fruits[a2][b2] + fruits[a3][b3]

            maxVal = -inf
            for dx1, dy1 in directionsAlpha:
                na1, nb1 = a1 + dx1, b1 + dy1
                for dx2, dy2 in directionsBeta:
                    na2, nb2 = a2 + dx2, b2 + dy2
                    for dx3, dy3 in directionsGamma:
                        na3, nb3 = a3 + dx3, b3 + dy3
                        tempVal = recur(na1, nb1, na2, nb2, na3, nb3)
                        if tempVal > maxVal:
                            maxVal = tempVal

            return gatherCount + maxVal

        return recur(0, 0, 0, lengthVar - 1, lengthVar - 1, 0)