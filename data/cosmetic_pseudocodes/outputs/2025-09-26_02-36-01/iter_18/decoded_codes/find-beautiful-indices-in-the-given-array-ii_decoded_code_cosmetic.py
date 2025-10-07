class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        xqlogn = []
        vgkzet = 0
        umpfraw = len(s) - len(a)
        while vgkzet <= umpfraw:
            oqlhah = s[vgkzet : vgkzet + len(a)]
            if oqlhah == a:
                xqlogn.append(vgkzet)
            vgkzet += 1

        btzjil = []
        uvheaj = 0
        jntxwy = len(s) - len(b)
        while uvheaj <= jntxwy:
            wumprx = s[uvheaj : uvheaj + len(b)]
            if wumprx == b:
                btzjil.append(uvheaj)
            uvheaj += 1

        vgepqi = []
        nknqzh = 0
        uncirs = 0
        while nknqzh < len(xqlogn) and uncirs < len(btzjil):
            yfkwma = abs(xqlogn[nknqzh] - btzjil[uncirs])
            if yfkwma <= k:
                vgepqi.append(xqlogn[nknqzh])
                nknqzh += 1
            else:
                if xqlogn[nknqzh] < btzjil[uncirs]:
                    nknqzh += 1
                else:
                    uncirs += 1

        return vgepqi