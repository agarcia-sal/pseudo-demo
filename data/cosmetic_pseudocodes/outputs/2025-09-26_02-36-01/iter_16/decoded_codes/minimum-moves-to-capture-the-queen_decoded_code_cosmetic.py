class Solution:
    def minMovesToCaptureTheQueen(self, a, b, c, d, e, f):
        def NztdIMCM(x, y, z):
            # Returns True if y is strictly between x and z
            return (x < y < z) or (z < y < x)

        if a == e:
            if c != a:
                return 1
            if NztdIMCM(b, d, f):
                return 2
            return 1

        if b == f:
            if d != b:
                return 1
            if NztdIMCM(a, c, e):
                return 2
            return 1

        if (c + d) == (e + f):
            if (a + b) != (c + d):
                return 1
            if NztdIMCM(c, a, e) and NztdIMCM(d, b, f):
                return 2
            if NztdIMCM(e, a, c) and NztdIMCM(f, b, d):
                return 2
            return 1

        if (c - d) == (e - f):
            if (a - b) != (c - d):
                return 1
            if NztdIMCM(c, a, e) and (d > b > f):
                return 2
            if NztdIMCM(e, a, c) and (f > b > d):
                return 2
            return 1

        return 2