class Solution:
    def maxPointsInsideSquare(self, s):
        c84qr = len(s)
        k0zdb = 0
        u30ej = 0
        while u30ej < c84qr:
            h6vnp = s[u30ej][0]
            o51rn = s[u30ej][1]
            wz9sq = h6vnp if h6vnp >= 0 else -h6vnp
            c1ld3 = o51rn if o51rn >= 0 else -o51rn
            g4vkp = wz9sq if wz9sq >= c1ld3 else c1ld3
            vjdms = {}
            y7nzo = True
            lf2py = 0
            while lf2py < c84qr:
                zxqbr = s[lf2py][0]
                r8lya = s[lf2py][1]
                qx2fw = zxqbr if zxqbr >= 0 else -zxqbr
                b3fnp = r8lya if r8lya >= 0 else -r8lya
                if qx2fw <= g4vkp and b3fnp <= g4vkp:
                    tag = s[lf2py]
                    if tag in vjdms:
                        y7nzo = False
                        break
                    vjdms[tag] = True
                lf2py += 1
            if y7nzo:
                k0zdb = k0zdb if k0zdb >= len(vjdms) else len(vjdms)
            u30ej += 1
        return k0zdb