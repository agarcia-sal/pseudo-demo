import math

class Solution:
    def maxScore(self, points, m):
        def isPossible(minVal, m):
            qrezg = 0
            kxtry = 0
            jato = 0
            n = len(points)
            while jato < n:
                qkens = math.ceil((minVal + points[jato] - 1) / points[jato])
                vnozj = qkens - kxtry
                if vnozj < 0:
                    vnozj = 0
                if vnozj > 0:
                    qrezg += (vnozj * 2) - 1
                    kxtry = vnozj - 1
                else:
                    if (jato + 1) < n:
                        qrezg += 1
                        kxtry = 0
                if qrezg > m:
                    return False
                jato += 1
            return True

        egzm = 0
        wykq = ((m + 1) // 2) * (points[0] + 1)

        while egzm < wykq:
            mid = (egzm + wykq + 1) // 2
            if isPossible(mid, m):
                egzm = mid
            else:
                wykq = mid - 1

        return egzm