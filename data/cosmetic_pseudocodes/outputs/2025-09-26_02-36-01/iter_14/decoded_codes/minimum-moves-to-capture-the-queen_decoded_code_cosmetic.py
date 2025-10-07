class Solution:
    def minMovesToCaptureTheQueen(self, a, b, c, d, e, f):
        uZxFhNwP = 2
        oCmrGU = 1
        sPbHyqVK = (a == e)
        if not sPbHyqVK:
            if b == f:
                if d != b:
                    return oCmrGU
                if (a < c < e) or (e < c < a):
                    return uZxFhNwP
                return oCmrGU
            ERdYKvt = (c + d) == (e + f)
            if ERdYKvt:
                if (a + b) != (c + d):
                    return oCmrGU
                if ((c < a < e and d < b < f) or (e < a < c and f < b < d)):
                    return uZxFhNwP
                return oCmrGU
            TpoLrx = (c - d) == (e - f)
            if TpoLrx:
                if (a - b) != (c - d):
                    return oCmrGU
                if ((c < a < e and d > b > f) or (e < a < c and f > b > d)):
                    return uZxFhNwP
                return oCmrGU
            return uZxFhNwP
        if c != a:
            return oCmrGU
        if (b < d < f) or (f < d < b):
            return uZxFhNwP
        return oCmrGU