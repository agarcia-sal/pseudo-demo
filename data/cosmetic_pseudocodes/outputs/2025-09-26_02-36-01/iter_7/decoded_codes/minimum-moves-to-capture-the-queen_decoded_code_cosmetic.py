class Solution:
    def minMovesToCaptureTheQueen(self, a, b, c, d, e, f):
        singleMove = 1
        doubleMove = singleMove + singleMove

        def outputSingle():
            return singleMove

        def outputDouble():
            return doubleMove

        def conditionOne(x, y, z):
            return (x < y < z) or (z < y < x)

        def sumsEqual(p, q, r, s):
            return (p + q) == (r + s)

        def differencesEqual(p, q, r, s):
            return (p - q) == (r - s)

        def sumsNotEqual(p, q, r, s):
            return not sumsEqual(p, q, r, s)

        def differencesNotEqual(p, q, r, s):
            return not differencesEqual(p, q, r, s)

        if a == e:
            if c != a:
                return outputSingle()
            else:
                if conditionOne(b, d, f):
                    return outputDouble()
                else:
                    return outputSingle()
        else:
            if b == f:
                if d != b:
                    return outputSingle()
                else:
                    if conditionOne(a, c, e):
                        return outputDouble()
                    else:
                        return outputSingle()
            else:
                if sumsEqual(c, d, e, f):
                    if sumsNotEqual(a, b, c, d):
                        return outputSingle()
                    else:
                        if ((c < a < e and d < b < f) or (e < a < c and f < b < d)):
                            return outputDouble()
                        else:
                            return outputSingle()
                else:
                    if differencesEqual(c, d, e, f):
                        if differencesNotEqual(a, b, c, d):
                            return outputSingle()
                        else:
                            if ((c < a < e and d > b > f) or (e < a < c and f > b > d)):
                                return outputDouble()
                            else:
                                return outputSingle()
                    else:
                        return outputDouble()