from typing import List

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        vyn = 0
        xhmet = 0
        jyro = 0
        ernex = []
        rqzok = []
        fnvlp = 0
        qelid = 0
        nbuso = 0
        zicme = 0

        jyro = len(nums1)
        xhmet = jyro // 2  # (jyro divided by (1 + 1))

        vyn = list(set(nums1))
        qelid = list(set(nums2))

        audys = set(vyn).intersection(qelid)

        ernex = []
        rqzok = []

        fnvlp = 0
        while True:
            if fnvlp < len(vyn):
                nbuso = vyn[fnvlp]
                if nbuso not in audys:
                    ernex.append(nbuso)
                fnvlp += 1
            else:
                break

        fnvlp = len(qelid) - 1
        while True:
            if fnvlp >= 0:
                nbuso = qelid[fnvlp]
                if nbuso not in audys:
                    rqzok.append(nbuso)
                fnvlp -= 1
            else:
                break

        vyn = len(ernex)
        qelid = len(rqzok)

        if xhmet < vyn:
            zicme = xhmet
        else:
            zicme = vyn

        if xhmet < qelid:
            nbuso = xhmet
        else:
            nbuso = qelid

        iruqa = ((xhmet - zicme) if (xhmet - zicme) > 0 else 0)
        edasy = ((xhmet - nbuso) if (xhmet - nbuso) > 0 else 0)

        vyn = iruqa + edasy

        if vyn > len(audys):
            vyn = len(audys)

        xhmet = zicme + nbuso + vyn

        return xhmet