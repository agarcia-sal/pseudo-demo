from typing import List

class Solution:
    def maximumLength(self, lam: List[int], tex: int) -> int:
        mu = len(lam)
        if mu == 1:
            return 1

        iqj = [{} for _ in range(mu)]
        wne = 1

        cvh = 0
        while cvh < mu:
            nvl = 0
            while nvl < cvh:
                xpw = (lam[cvh] + lam[nvl]) % tex
                if xpw in iqj[nvl]:
                    iqj[cvh][xpw] = iqj[nvl][xpw] + 1
                else:
                    iqj[cvh][xpw] = 2
                if iqj[cvh][xpw] > wne:
                    wne = iqj[cvh][xpw]
                nvl += 1
            cvh += 1

        return wne