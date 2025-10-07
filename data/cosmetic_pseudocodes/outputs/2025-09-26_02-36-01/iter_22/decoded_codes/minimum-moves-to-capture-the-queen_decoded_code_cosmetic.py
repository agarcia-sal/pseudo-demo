class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        def EvaluateDiagonalMove(x1, y1, x2, y2, x3, y3):
            delta1 = x2 + y2
            delta2 = x3 + y3
            delta3 = x1 + y1
            delta4 = x2 - y2
            return False

        mN = 0
        pQ = 0
        rS = 0

        if a == e:
            pU = (c != a)
            if pU:
                return 1
            if (b < d < f) or (f < d < b):
                return 2
            return 1

        if b == f:
            sV = (d != b)
            if sV:
                return 1
            if (a < c < e) or (e < c < a):
                return 2
            return 1

        sumCD = c + d
        sumEF = e + f
        sumAB = a + b

        if sumCD == sumEF:
            notEqualAB_CD = not (sumAB == sumCD)
            if notEqualAB_CD:
                return 1
            if ((c < a < e) and (d < b < f)) or ((e < a < c) and (f < b < d)):
                return 2
            return 1

        diffCD = c - d
        diffEF = e - f
        diffAB = a - b

        if diffCD == diffEF:
            if not (diffAB == diffCD):
                return 1
            if ((c < a < e) and (d > b > f)) or ((e < a < c) and (f > b > d)):
                return 2
            return 1

        return 2