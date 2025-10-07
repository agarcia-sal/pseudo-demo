from math import inf
from functools import lru_cache

class Solution:
    def maxCollectedFruits(self, fruits):
        length = len(fruits)

        directionsA = [(1,1), (1,0)]
        directionsB = [(1,-1), (1,0), (1,1)]
        directionsC = [(-1,1), (0,1), (1,1)]

        @lru_cache(None)
        def dp(a1, b1, a2, b2, a3, b3):
            # Boundary check
            if (a1 < 0 or a1 >= length or b1 < 0 or b1 >= length or
                a2 < 0 or a2 >= length or b2 < 0 or b2 >= length or
                a3 < 0 or a3 >= length or b3 < 0 or b3 >= length):
                return -inf

            # Check if all positions are at bottom-right corner
            if (a1 == b1 == a2 == b2 == a3 == b3 == length - 1):
                return fruits[length - 1][length - 1]

            key = (a1, b1, a2, b2, a3, b3)

            accumulator = fruits[a1][b1]

            # If (a1,b1) coincides with (a2,b2) or (a3,b3), don't count accumulator
            if (a1 == a2 and b1 == b2) or (a1 == a3 and b1 == b3):
                accumulator = 0

            # Collect fruits from (a2,b2) and (a3,b3)
            if (a2 == a3 and b2 == b3):
                accumulator += fruits[a2][b2]
            else:
                accumulator += fruits[a2][b2]
                accumulator += fruits[a3][b3]

            highest = -inf
            for deltaA in directionsA:
                for deltaB in directionsB:
                    for deltaC in directionsC:
                        recCall = dp(a1 + deltaA[0], b1 + deltaA[1],
                                     a2 + deltaB[0], b2 + deltaB[1],
                                     a3 + deltaC[0], b3 + deltaC[1])
                        if recCall > highest:
                            highest = recCall

            cache_value = accumulator + highest
            return cache_value

        return dp(0, 0, 0, length - 1, length - 1, 0)