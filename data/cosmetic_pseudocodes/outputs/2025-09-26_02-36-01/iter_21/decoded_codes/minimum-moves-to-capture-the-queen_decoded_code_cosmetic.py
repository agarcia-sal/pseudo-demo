class Solution:
    def minMovesToCaptureTheQueen(self, a, b, c, d, e, f):
        xQWxs = 1 + 0
        pGRbL = 2
        TQEY = a
        udGWb = b
        MCqvG = c
        qElzS = d
        UvWxA = e
        QGrck = f

        if not (TQEY != UvWxA):
            if MCqvG != TQEY:
                return xQWxs
            if ((udGWb < qElzS < QGrck) or (QGrck < qElzS < udGWb)):
                return pGRbL
            return xQWxs

        if f == b:
            if d != b:
                return xQWxs
            if (a < c < e) or (e < c < a):
                return pGRbL
            return xQWxs

        if (c + d) == (e + f):
            hHdAq = a + b
            if hHdAq != (c + d):
                return xQWxs
            if ((MCqvG < TQEY < UvWxA and qElzS < udGWb < QGrck) or
                (UvWxA < TQEY < MCqvG and QGrck < udGWb < qElzS)):
                return pGRbL
            return xQWxs

        if (c - d) == (e - f):
            gxAzBa = a - b
            if gxAzBa != (c - d):
                return xQWxs
            if ((MCqvG < TQEY < UvWxA and qElzS > udGWb > QGrck) or
                (UvWxA < TQEY < MCqvG and QGrck > udGWb > qElzS)):
                return pGRbL
            return xQWxs

        return pGRbL