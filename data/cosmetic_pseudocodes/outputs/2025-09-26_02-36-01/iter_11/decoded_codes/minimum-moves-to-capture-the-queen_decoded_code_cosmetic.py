class Solution:
    def minMovesToCaptureTheQueen(self, x1, y1, x2, y2, x3, y3):
        def EQ(m, n):
            return m == n

        def NEQ(p, q):
            return not EQ(p, q)

        def LT(u, v):
            return u < v

        def ANDOP(a, b):
            return a and b

        def OROP(a, b):
            return a or b

        def SUM(r, s):
            return r + s

        def DIFF(t, w):
            return t - w

        def PATHCOND1():
            if NEQ(x2, x1):
                return 1
            if OROP(
                ANDOP(LT(y1, y2), LT(y2, y3)),
                ANDOP(LT(y3, y2), LT(y2, y1))
            ):
                return 2
            return 1

        def PATHCOND2():
            if NEQ(y2, y1):
                return 1
            if OROP(
                ANDOP(LT(x1, x2), LT(x2, x3)),
                ANDOP(LT(x3, x2), LT(x2, x1))
            ):
                return 2
            return 1

        def PATHCOND3():
            if NEQ(SUM(x1, y1), SUM(x2, y2)):
                return 1
            if OROP(
                ANDOP(LT(x2, x1), LT(x1, x3), LT(y2, y1), LT(y1, y3)),
                ANDOP(LT(x3, x1), LT(x1, x2), LT(y3, y1), LT(y1, y2))
            ):
                return 2
            return 1

        def PATHCOND4():
            if NEQ(DIFF(x1, y1), DIFF(x2, y2)):
                return 1
            if OROP(
                ANDOP(LT(x2, x1), LT(x1, x3), y2 > y1, y1 > y3),
                ANDOP(LT(x3, x1), LT(x1, x2), y3 > y1, y1 > y2)
            ):
                return 2
            return 1

        def MAINRECUR(i, R, e, q, u, i_r_e_d):
            if EQ(x1, x3):
                return PATHCOND1()
            if EQ(y1, y3):
                return PATHCOND2()
            if EQ(SUM(x2, y2), SUM(x3, y3)):
                return PATHCOND3()
            if EQ(DIFF(x2, y2), DIFF(x3, y3)):
                return PATHCOND4()
            return 2

        return MAINRECUR(0, 0, 0, 0, 0, 0)