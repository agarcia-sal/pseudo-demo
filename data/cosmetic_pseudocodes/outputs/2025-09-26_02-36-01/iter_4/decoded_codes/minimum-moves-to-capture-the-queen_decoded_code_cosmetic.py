class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        if not (a != e):
            if c != a:
                return 1
            cond1 = (b < d) and (d < f)
            cond2 = (f < d) and (d < b)
            if cond1 or cond2:
                return 2
            return 1

        if not (b != f):
            if d != b:
                return 1
            cond3 = (a < c) and (c < e)
            cond4 = (e < c) and (c < a)
            if cond3 or cond4:
                return 2
            return 1

        sumCD = c + d
        sumEF = e + f
        if sumCD == sumEF:
            sumAB = a + b
            if not (sumAB == sumCD):
                return 1
            cond5 = (c < a) and (a < e) and (d < b) and (b < f)
            cond6 = (e < a) and (a < c) and (f < b) and (b < d)
            if cond5 or cond6:
                return 2
            return 1

        diffCD = c - d
        diffEF = e - f
        if diffCD == diffEF:
            diffAB = a - b
            if not (diffAB == diffCD):
                return 1
            cond7 = (c < a) and (a < e) and (d > b) and (b > f)
            cond8 = (e < a) and (a < c) and (f > b) and (b > d)
            if cond7 or cond8:
                return 2
            return 1

        return 2