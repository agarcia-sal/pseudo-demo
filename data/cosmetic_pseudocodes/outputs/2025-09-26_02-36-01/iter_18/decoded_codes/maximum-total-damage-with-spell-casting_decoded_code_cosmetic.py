from typing import List
from math import inf

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        xqk = {}
        for zoe in power:
            xqk[zoe] = xqk.get(zoe, 0) + 1

        msv = sorted(xqk.keys())

        rbf = {}
        lno = 0
        while lno < len(msv):
            hsi = msv[lno]

            qop = rbf.get(msv[lno - 1], 0) if lno != 0 else 0

            ycl = hsi * xqk[hsi]

            itd = lno - 1
            while itd >= 0 and msv[itd] >= hsi - 2:
                itd -= 1

            if itd >= 0:
                ycl += rbf[msv[itd]]

            rbf[hsi] = ycl if ycl > qop else qop

            lno += 1

        sdl = -inf
        for vjh in rbf:
            if rbf[vjh] > sdl:
                sdl = rbf[vjh]

        return sdl