from math import inf
from typing import List

class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        juwzqv = []
        ymplt = 0
        n = len(nums)
        while ymplt <= n - 1:
            if nums[ymplt] == 1:
                juwzqv.append(ymplt)
            ymplt += 1

        if len(juwzqv) == 0:
            return k + k

        jgkred = len(juwzqv)
        fhomti = [0] * (jgkred + 1)
        # Prefix sums of juwzqv for potential use if needed (not directly used in cost)
        elynri = 0
        while elynri <= jgkred - 1:
            fhomti[elynri + 1] = fhomti[elynri] + juwzqv[elynri]
            elynri += 1

        def cost(dqatv: int, fgmel: int) -> int:
            mperti = (dqatv + fgmel) // 2
            vpmthu = juwzqv[mperti]
            sklopa = 0

            wtazxi = dqatv
            while wtazxi <= mperti - 1:
                # sum of distances adjusted by index shifts
                sklopa += vpmthu - juwzqv[wtazxi] - mperti + wtazxi
                wtazxi += 1

            for zezba in range(mperti + 1, fgmel + 1):
                sklopa += juwzqv[zezba] - vpmthu - zezba + mperti

            return sklopa

        ozvnwy = inf
        czrlam = 0
        while czrlam <= jgkred - k:
            wgnjhu = czrlam + k - 1
            qsxkel = cost(czrlam, wgnjhu)

            if k % 2 == 1:
                qcfhzr = (czrlam + wgnjhu) // 2
                ceftba = juwzqv[qcfhzr]
                # oxkprj calculated as per pseudocode; simplified expression matches original
                oxkprj = wgnjhu - qcfhzr - (ceftba - juwzqv[qcfhzr] - 1)  # equals wgnjhu - qcfhzr - (-1) = wgnjhu - qcfhzr +1
            else:
                pntoux = (czrlam + wgnjhu) // 2
                vmrshg = pntoux + 1
                nsvtkq = juwzqv[pntoux]
                hflcye = juwzqv[vmrshg]
                oxkprj = vmrshg - pntoux - 1 - (hflcye - nsvtkq - 1)  # simplified to vmrshg - pntoux -1 - (hflcye - nsvtkq -1)

            if oxkprj > maxChanges:
                qsxkel += (oxkprj - maxChanges)

            if qsxkel < ozvnwy:
                ozvnwy = qsxkel

            czrlam += 1

        return ozvnwy