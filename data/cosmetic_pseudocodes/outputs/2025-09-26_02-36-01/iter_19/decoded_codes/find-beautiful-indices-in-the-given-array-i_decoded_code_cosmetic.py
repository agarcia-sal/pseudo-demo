class Solution:
    def beautifulIndices(self, s, a, b, k):
        x1 = []
        m = len(s)
        n = len(a)
        u = 0
        while u <= m - n:
            v = 0
            w = True
            while v < n:
                if s[u + v] != a[v]:
                    w = False
                    break
                v += 1
            if w:
                x1.append(u)
            u += 1

        y1 = []
        p = len(b)
        q = 0
        while q <= m - p:
            r = 0
            t = True
            while r < p:
                if s[q + r] != b[r]:
                    t = False
                    break
                r += 1
            if t:
                y1.append(q)
            q += 1

        z1 = []
        for e1 in x1:
            c1 = False
            f1 = 0
            while f1 < len(y1) and not c1:
                if (y1[f1] - e1) * (e1 - y1[f1]) >= -k * k:
                    z1.append(e1)
                    c1 = True
                f1 += 1

        return z1