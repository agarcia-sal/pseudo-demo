from math import inf
from functools import lru_cache

class Solution:
    def maxCollectedFruits(self, fruits):
        lengthGrid = len(fruits)

        directionsOne = [(1, 1), (1, 0)]
        directionsTwo = [(1, -1), (1, 0), (1, 1)]
        directionsThree = [(-1, 1), (0, 1), (1, 1)]

        @lru_cache(None)
        def dp(xA, yA, xB, yB, xC, yC):
            # Out of bounds check
            if not (0 <= xA < lengthGrid and 0 <= yA < lengthGrid and
                    0 <= xB < lengthGrid and 0 <= yB < lengthGrid and
                    0 <= xC < lengthGrid and 0 <= yC < lengthGrid):
                return -inf

            # Terminal position
            if (xA == yA == xB == yB == xC == yC == lengthGrid - 1):
                return fruits[lengthGrid - 1][lengthGrid - 1]

            stateKey = (xA, yA, xB, yB, xC, yC)  # cached automatically by lru_cache

            sumCollected = fruits[xA][yA]

            # If A shares position with B or C, A collects no fruits in this cell
            if (xA == xB and yA == yB) or (xA == xC and yA == yC):
                sumCollected = 0

            # Collection for B and C
            if xB == xC and yB == yC:
                sumCollected += fruits[xB][yB]
            else:
                sumCollected += fruits[xB][yB] + fruits[xC][yC]

            maxNextFruits = -inf
            for deltaXA, deltaYA in directionsOne:
                nxA, nyA = xA + deltaXA, yA + deltaYA
                for deltaXB, deltaYB in directionsTwo:
                    nxB, nyB = xB + deltaXB, yB + deltaYB
                    for deltaXC, deltaYC in directionsThree:
                        nxC, nyC = xC + deltaXC, yC + deltaYC
                        candidate = dp(nxA, nyA, nxB, nyB, nxC, nyC)
                        if candidate > maxNextFruits:
                            maxNextFruits = candidate

            totalCollected = sumCollected + maxNextFruits
            return totalCollected

        return dp(0, 0, 0, lengthGrid - 1, lengthGrid - 1, 0)