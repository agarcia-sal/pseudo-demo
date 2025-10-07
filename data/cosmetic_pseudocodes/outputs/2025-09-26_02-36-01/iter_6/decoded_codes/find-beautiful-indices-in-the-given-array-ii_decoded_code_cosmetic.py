class Solution:
    def beautifulIndices(self, s: str, x: str, y: str, z: int) -> list[int]:
        p = []
        m = len(s) - len(x)
        q = 0
        while q <= m:
            r = q + len(x) - 1
            u = s[q : r + 1]
            if u == x:
                p.append(q)
            q += 1

        v = []
        n = len(s) - len(y)
        t = 0
        while t <= n:
            w = t + len(y) - 1
            o = s[t : w + 1]
            if o == y:
                v.append(t)
            t += 1

        c = []

        def loopHelper(a: int, b: int, f: list[int], g: list[int], h: list[int]) -> list[int]:
            if a >= len(f) or b >= len(g):
                return h
            s1 = f[a]
            s2 = g[b]
            diffTemp = s1 - s2
            diffValue = -diffTemp if diffTemp < 0 else diffTemp
            if diffValue <= z:
                h.append(s1)
                return loopHelper(a + 1, b, f, g, h)
            else:
                if s1 < s2:
                    return loopHelper(a + 1, b, f, g, h)
                else:
                    return loopHelper(a, b + 1, f, g, h)

        d = 0
        e = 0
        return loopHelper(d, e, p, v, c)