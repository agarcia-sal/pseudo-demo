from math import inf
from typing import List, Tuple

class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        lengthVar = len(fruits)
        delta1 = [(1,1),(1,0),(0,1)]
        delta2 = [(1,0),(1,-1),(1,1)]
        delta3 = [(-1,1),(0,1),(1,1)]
        cacheStore = {}

        def explore(a: int, b: int, c: int, d: int, e: int, f: int) -> int:
            # Boundary checks
            if (a < 0 or a >= lengthVar or b < 0 or b >= lengthVar or
                c < 0 or c >= lengthVar or d < 0 or d >= lengthVar or
                e < 0 or e >= lengthVar or f < 0 or f >= lengthVar):
                return -inf

            # Termination condition: all positions at bottom-right corner
            if a == b == c == d == e == f == lengthVar - 1:
                return fruits[lengthVar - 1][lengthVar - 1]

            keyTuple = (a, b, c, d, e, f)
            if keyTuple in cacheStore:
                return cacheStore[keyTuple]

            gatherCount = fruits[a][b]

            # Avoid double counting: if (a,b) equals (c,d) or (e,f), zero out initial gatherCount
            if (a == c and b == d) or (a == e and b == f):
                gatherCount = 0

            # Add fruits for (c,d) and (e,f)
            if e == c and f == d:
                gatherCount += fruits[c][d]
            else:
                gatherCount += fruits[c][d] + fruits[e][f]

            bestVal = -inf
            for dxA, dyA in delta1:
                a_new, b_new = a + dxA, b + dyA
                for dxB, dyB in delta2:
                    c_new, d_new = c + dxB, d + dyB
                    for dxC, dyC in delta3:
                        e_new, f_new = e + dxC, f + dyC
                        tempVal = explore(a_new, b_new, c_new, d_new, e_new, f_new)
                        if tempVal > bestVal:
                            bestVal = tempVal

            cacheStore[keyTuple] = gatherCount + bestVal
            return cacheStore[keyTuple]

        return explore(0, 0, 0, lengthVar - 1, lengthVar - 1, 0)