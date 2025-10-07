class Solution:
    def minMovesToCaptureTheQueen(self, a, b, c, d, e, f):
        def eq(x, y):
            return x == y

        def neq(x, y):
            return not eq(x, y)

        def lt(x, y):
            return x < y

        def gt(x, y):
            return y < x

        def and_(x, y):
            return x and y

        def or_(x, y):
            return x or y

        def insideRange(u, v, w):
            return or_(and_(lt(v, u), lt(u, w)), and_(lt(w, u), lt(u, v)))

        def checkMiddle(p, q, r, s, t, u):
            if eq(p, s):
                if neq(r, p):
                    return 1
                if or_(and_(lt(q, t), lt(t, u)), and_(lt(u, t), lt(t, q))):
                    return 2
                return 1
            return 0

        def checkSum(x1, y1, x2, y2, x3, y3):
            if eq(x1 + y1, x3 + y3):
                if neq(x2 + y2, x1 + y1):
                    return 1
                if or_(
                    and_(lt(x2, x1), lt(x1, x3), and_(lt(y2, y1), lt(y1, y3))) or
                    (lt(x3, x1) and lt(x1, x2) and lt(y3, y1) and lt(y1, y2))
                ):
                    return 2
                return 1
            return 0

        def checkDiff(a1, b1, a2, b2, a3, b3):
            if eq(a1 - b1, a3 - b3):
                if neq(a2 - b2, a1 - b1):
                    return 1
                if or_(
                    and_(lt(a2, a1), lt(a1, a3), and_(gt(b2, b1), gt(b1, b3))) or
                    (lt(a3, a1) and lt(a1, a2) and gt(b3, b1) and gt(b1, b2))
                ):
                    return 2
                return 1
            return 0

        r1 = checkMiddle(a, b, c, d, e, f)
        if r1 > 0:
            return r1

        r2 = 0
        if eq(b, f):
            if neq(d, b):
                return 1
            if or_(and_(lt(a, c), lt(c, e)), and_(lt(e, c), lt(c, a))):
                return 2
            return 1

        r3 = checkSum(a, b, c, d, e, f)
        if r3 > 0:
            return r3

        r4 = checkDiff(c, d, e, f, a, b)
        if r4 > 0:
            return r4

        return 2