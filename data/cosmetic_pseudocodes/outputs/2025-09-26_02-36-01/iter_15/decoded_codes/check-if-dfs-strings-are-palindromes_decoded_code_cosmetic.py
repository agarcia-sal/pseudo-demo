class Hashing:
    def __init__(self, s, base, mod):
        xg = mod
        n = len(s)
        qb = [0] * (n + 1)
        mrl = [1] * (n + 1)
        uj = 1
        while uj <= n:
            hd = (qb[uj - 1] * base + ord(s[uj - 1])) % xg
            qb[uj] = hd
            mrl[uj] = (mrl[uj - 1] * base) % xg
            uj += 1
        self.mod = xg
        self.h = qb
        self.p = mrl

    def query(self, l, r):
        rt = (self.h[r] - self.h[l - 1] * self.p[r - l + 1]) % self.mod
        return rt


class Solution:
    def findAnswer(self, parent, s):
        ag = len(s)
        nx = [[] for _ in range(ag)]
        zp = 1
        while zp < ag:
            nx[parent[zp]].append(zp)
            zp += 1

        bk = []
        ox = {}

        def dfs(i):
            ct = len(bk) + 1
            for child in nx[i]:
                dfs(child)
            bk.append(s[i])
            ys = len(bk)
            ox[i] = (ct, ys)

        dfs(0)

        base = 33331
        modulus = 998244353
        qk = Hashing(bk, base, modulus)

        reversedBk = bk[::-1]
        wt = Hashing(reversedBk, base, modulus)

        ji = []
        uv = 0
        while uv < ag:
            l, r = ox[uv]
            fz = r - l + 1
            half = fz // 2
            mn = qk.query(l, l + half - 1) if half > 0 else 0
            dz = wt.query(ag - r + 1, ag - r + half) if half > 0 else 0
            ji.append(mn == dz)
            uv += 1
        return ji