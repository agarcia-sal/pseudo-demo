class Solution:
    def minMovesToCaptureTheQueen(self, a, b, c, d, e, f):
        x = 2
        y = 1

        shouldReturn = False
        result = x

        if a == e:
            if c != a:
                result = y
                shouldReturn = True
            if ((b < d < f) or (f < d < b)) and not shouldReturn:
                result = x
                shouldReturn = True
            if not shouldReturn:
                result = y
                shouldReturn = True

        elif b == f:
            if d != b:
                result = y
                shouldReturn = True
            if ((a < c < e) or (e < c < a)) and not shouldReturn:
                result = x
                shouldReturn = True
            if not shouldReturn:
                result = y
                shouldReturn = True

        elif (c + d) == (e + f):
            if (a + b) != (c + d):
                result = y
                shouldReturn = True
            if (((c < a < e) and (d < b < f)) or ((e < a < c) and (f < b < d))) and not shouldReturn:
                result = x
                shouldReturn = True
            if not shouldReturn:
                result = y
                shouldReturn = True

        elif (c - d) == (e - f):
            if (a - b) != (c - d):
                result = y
                shouldReturn = True
            if (((c < a < e) and (d > b > f)) or ((e < a < c) and (f > b > d))) and not shouldReturn:
                result = x
                shouldReturn = True
            if not shouldReturn:
                result = y
                shouldReturn = True

        else:
            result = x
            shouldReturn = True

        return result