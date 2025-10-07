from typing import List

class Solution:
    def minMoves(self, rooks: List[List[int]]) -> int:
        x1 = len(rooks)
        y3 = sorted(rooks, key=lambda a: a[0])
        z7 = sorted(rooks, key=lambda c: c[1])
        wq = 0
        v5 = 0

        for kp in range(x1):
            h2 = y3[kp][0]
            jb = kp
            u9 = abs(h2 - jb)
            wq += u9

        for la in range(x1):
            re = z7[la][1]
            n0 = la
            mp = abs(re - n0)
            v5 += mp

        return wq + v5